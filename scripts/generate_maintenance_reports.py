#!/usr/bin/env python3
"""Generate deterministic coverage, API, benchmark, permission, and archive reports."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import yaml

from check_catalog import translation_debts
from generate_catalog import CatalogError, load_catalog


ROOT = Path(__file__).resolve().parents[1]


class MaintenanceError(ValueError):
    """A maintenance report cannot be produced from the supplied evidence."""


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise MaintenanceError(f"{path} must contain a mapping")
    return value


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise MaintenanceError(f"{path} must contain an object")
    return value


def generated_at() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def finding(identity: str, severity: str, message: str, **evidence: Any) -> dict[str, Any]:
    result = {"id": identity, "severity": severity, "message": message}
    if evidence:
        result["evidence"] = evidence
    return result


def report(kind: str, findings: list[dict], summary: dict, status: str | None = None) -> dict:
    return {
        "schema_version": 1,
        "kind": kind,
        "generated_at": generated_at(),
        "status": status or ("pass" if not findings else "attention"),
        "summary": summary,
        "findings": findings,
    }


def percentage(numerator: int, denominator: int) -> float:
    """Return a deterministic percentage for report summaries."""
    return round(100 * numerator / denominator, 2) if denominator else 100.0


def load_git_yaml(repository: Path, target_ref: str, path: str) -> dict[str, Any]:
    content = git_blob(repository, target_ref, path)
    if content is None:
        raise MaintenanceError(f"{path} is missing at {target_ref}")
    value = yaml.safe_load(content.decode("utf-8"))
    if not isinstance(value, dict):
        raise MaintenanceError(f"{path} at {target_ref} must contain a mapping")
    return value


def git_tree_paths(repository: Path, target_ref: str) -> set[str]:
    result = git(repository, "ls-tree", "-r", "--name-only", "-z", target_ref)
    return {
        item.decode("utf-8")
        for item in result.stdout.split(b"\0")
        if item
    }


def git_document_blob(repository: Path, target_ref: str, path: str) -> bytes | None:
    """Read a tracked document, following an in-repository Git symlink."""
    content = git_blob(repository, target_ref, path)
    if content is None:
        return None
    listing = git(
        repository,
        "ls-tree",
        target_ref,
        "--",
        path,
        check=False,
    )
    line = listing.stdout.decode("utf-8", errors="replace").strip()
    if not line.startswith("120000 blob "):
        return content
    target = content.decode("utf-8", errors="strict").strip()
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), target))
    if posixpath.isabs(resolved) or resolved == ".." or resolved.startswith("../"):
        return None
    return git_blob(repository, target_ref, resolved)


def is_markdown_path(path: str) -> bool:
    return Path(path).suffix.lower() in {".md", ".markdown", ".mdown", ".mkd"}


def catalog_page_url(catalog: dict, page: dict) -> str:
    site = catalog.get("site", {})
    base_url = str(site.get("base_url", "")).rstrip("/") + "/"
    default_language = site.get("default_language", "zh_CN")
    language_prefix = "" if page["language"] == default_language else f"{page['language']}/"
    page_path = page["path"]
    if page_path == "index.md":
        relative = ""
    elif page_path.endswith("/index.md"):
        relative = page_path[: -len("index.md")]
    elif page_path.endswith(".md"):
        relative = page_path[:-3].rstrip("/") + "/"
    else:
        relative = page_path.rstrip("/") + "/"
    return urllib.parse.urljoin(base_url, language_prefix + relative)


def add_coverage_regression(
    findings: list[dict],
    dimension: str,
    covered: int,
    expected: int,
    **evidence: Any,
) -> None:
    if covered >= expected:
        return
    findings.append(
        finding(
            f"docs-coverage-regression:{dimension}",
            "error",
            f"{dimension} coverage fell to {covered}/{expected}.",
            coverage_percent=percentage(covered, expected),
            **evidence,
        )
    )


def source_documentation_coverage(
    source_repo: Path,
    target_ref: str,
    catalog: dict,
) -> tuple[list[dict], dict[str, Any]]:
    """Reconcile CCB's live registry and frozen migration baseline with the catalog."""
    registry_path = "ai/documentation-registry.yml"
    inventory_path = "doc/migration/markdown-inventory.yml"
    registry = load_git_yaml(source_repo, target_ref, registry_path)
    inventory = load_git_yaml(source_repo, target_ref, inventory_path)
    source_commit = git_text(source_repo, "rev-parse", target_ref)
    tracked_paths = git_tree_paths(source_repo, target_ref)
    tracked_markdown = {path for path in tracked_paths if is_markdown_path(path)}
    findings: list[dict] = []

    entries = registry.get("entries")
    if not isinstance(entries, list):
        raise MaintenanceError(f"{registry_path} entries must be a list")
    entry_paths = [
        entry.get("path")
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("path"), str)
    ]
    valid_entry_paths = {path for path in entry_paths if isinstance(path, str) and path}
    entry_ids = [
        entry.get("id")
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("id"), str)
    ]
    duplicate_registry_paths = sorted(
        path for path, count in Counter(entry_paths).items() if path and count > 1
    )
    duplicate_registry_ids = sorted(
        identity for identity, count in Counter(entry_ids).items() if identity and count > 1
    )
    declared_entry_count = registry.get("entry_count")
    if declared_entry_count != len(entries):
        findings.append(
            finding(
                "documentation-registry-entry-count",
                "error",
                "CCB documentation registry entry_count does not match its entries.",
                declared=declared_entry_count,
                actual=len(entries),
            )
        )
    if duplicate_registry_paths or duplicate_registry_ids:
        findings.append(
            finding(
                "documentation-registry-duplicates",
                "error",
                "CCB documentation registry contains duplicate paths or IDs.",
                duplicate_paths=duplicate_registry_paths,
                duplicate_ids=duplicate_registry_ids,
            )
        )
    unregistered_markdown = sorted(tracked_markdown - valid_entry_paths)
    if unregistered_markdown:
        findings.append(
            finding(
                "unregistered-markdown",
                "error",
                "Tracked CCB Markdown is absent from ai/documentation-registry.yml.",
                count=len(unregistered_markdown),
                paths=unregistered_markdown,
            )
        )
    registered_markdown = len(tracked_markdown & valid_entry_paths)
    add_coverage_regression(
        findings,
        "documentation-registry",
        registered_markdown,
        len(tracked_markdown),
        unregistered_paths=unregistered_markdown,
    )
    missing_registry_paths = sorted(valid_entry_paths - tracked_paths)
    if missing_registry_paths:
        findings.append(
            finding(
                "documentation-registry-missing-paths",
                "error",
                "CCB documentation registry names paths absent from the target commit.",
                count=len(missing_registry_paths),
                paths=missing_registry_paths,
            )
        )

    documents = inventory.get("documents")
    if not isinstance(documents, list):
        raise MaintenanceError(f"{inventory_path} documents must be a list")
    declared_document_count = inventory.get("document_count")
    if declared_document_count != 175 or len(documents) != 175:
        findings.append(
            finding(
                "frozen-markdown-inventory-size",
                "error",
                "The frozen Markdown migration baseline must remain exactly 175 documents.",
                declared=declared_document_count,
                actual=len(documents),
            )
        )
    original_paths = [
        document.get("original_path")
        for document in documents
        if isinstance(document, dict)
    ]
    duplicate_inventory_paths = sorted(
        path for path, count in Counter(original_paths).items() if path and count > 1
    )
    if duplicate_inventory_paths:
        findings.append(
            finding(
                "frozen-markdown-inventory-duplicates",
                "error",
                "The frozen Markdown migration baseline contains duplicate original paths.",
                paths=duplicate_inventory_paths,
            )
        )
    valid_documents = [document for document in documents if isinstance(document, dict)]
    inventory_registered = sum(
        document.get("original_path") in valid_entry_paths for document in valid_documents
    )
    missing_inventory_registry = sorted(
        str(document.get("original_path"))
        for document in valid_documents
        if document.get("original_path") not in valid_entry_paths
    )
    add_coverage_regression(
        findings,
        "frozen-inventory-registration",
        inventory_registered,
        len(valid_documents),
        missing_paths=missing_inventory_registry,
    )
    terminal_statuses = {"verified", "stubbed", "archived"}
    terminal_documents = [
        document
        for document in valid_documents
        if document.get("migration_status") in terminal_statuses
    ]
    nonterminal = sorted(
        str(document.get("original_path"))
        for document in valid_documents
        if document.get("migration_status") not in terminal_statuses
    )
    add_coverage_regression(
        findings,
        "frozen-inventory-terminal-state",
        len(terminal_documents),
        len(valid_documents),
        nonterminal_paths=nonterminal,
    )

    registry_by_path = {
        entry["path"]: entry
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("path"), str)
    }
    permanent_entries = [
        document
        for document in valid_documents
        if document.get("migration_status") in {"stubbed", "archived"}
    ]
    invalid_stubs: list[dict[str, Any]] = []
    verified_stubs = 0
    for document in permanent_entries:
        path = document.get("original_path")
        entry = registry_by_path.get(path)
        content = (
            git_document_blob(source_repo, target_ref, path)
            if isinstance(path, str)
            else None
        )
        expected_registry_status = (
            "archived" if document.get("migration_status") == "archived" else "moved_stub"
        )
        required_values = [
            "<!-- CCB-DOC-MOVED-START -->",
            document.get("stable_document_id"),
            document.get("source_commit"),
            document.get("zh_url"),
            document.get("en_url"),
            document.get("moved_at"),
            "no longer maintained",
        ]
        decoded = content.decode("utf-8", errors="replace") if content is not None else ""
        missing_values = [
            str(value)
            for value in required_values
            if not isinstance(value, str) or not value or value not in decoded
        ]
        problems: list[str] = []
        if content is None:
            problems.append("tracked stub path missing")
        if not entry:
            problems.append("registry entry missing")
        elif entry.get("status") != expected_registry_status:
            problems.append(
                f"registry status is {entry.get('status')!r}, expected {expected_registry_status!r}"
            )
        if missing_values:
            problems.append("stub metadata or permanent notice missing")
        if problems:
            invalid_stubs.append(
                {
                    "path": path,
                    "problems": problems,
                    "missing_values": missing_values,
                }
            )
        else:
            verified_stubs += 1
    if invalid_stubs:
        findings.append(
            finding(
                "permanent-migration-stubs-invalid",
                "error",
                "Migrated or archived CCB paths lack a complete permanent bilingual entry.",
                count=len(invalid_stubs),
                entries=invalid_stubs,
            )
        )
    add_coverage_regression(
        findings,
        "permanent-migration-stubs",
        verified_stubs,
        len(permanent_entries),
        invalid_paths=[item["path"] for item in invalid_stubs],
    )

    catalog_pages = catalog.get("pages", [])
    catalog_by_key: dict[tuple[str, str], dict] = {}
    duplicate_catalog_keys: list[str] = []
    for page in catalog_pages:
        if not isinstance(page, dict):
            continue
        key = (page.get("id"), page.get("language"))
        if not all(isinstance(value, str) for value in key):
            continue
        if key in catalog_by_key:
            duplicate_catalog_keys.append(f"{key[0]}:{key[1]}")
        catalog_by_key[key] = page
    if duplicate_catalog_keys:
        findings.append(
            finding(
                "docs-catalog-duplicate-language-ids",
                "error",
                "CCB-Docs catalog has duplicate (id, language) keys.",
                keys=sorted(duplicate_catalog_keys),
            )
        )
    bilingual_catalog_ids = {
        identity
        for identity, _language in catalog_by_key
        if {
            language
            for candidate, language in catalog_by_key
            if candidate == identity
        }
        >= {"zh_CN", "en"}
    }
    context_catalog_references = 0
    context_catalog_resolved = 0
    unresolved_context_ids: list[dict[str, str]] = []
    context_specs = (
        ("ai/task-router.yml", "entries", "documentation_ids"),
        ("ai/agent-benchmark.yml", "cases", "expected_documentation_ids"),
    )
    for path, collection_key, ids_key in context_specs:
        context = load_git_yaml(source_repo, target_ref, path)
        records = context.get(collection_key)
        if not isinstance(records, list):
            raise MaintenanceError(f"{path} {collection_key} must be a list")
        for record in records:
            if not isinstance(record, dict):
                continue
            for identity in record.get(ids_key, []):
                if not isinstance(identity, str):
                    continue
                context_catalog_references += 1
                if identity in bilingual_catalog_ids:
                    context_catalog_resolved += 1
                else:
                    unresolved_context_ids.append(
                        {
                            "path": path,
                            "record_id": str(record.get("id")),
                            "document_id": identity,
                        }
                    )
    if unresolved_context_ids:
        findings.append(
            finding(
                "agent-context-unresolved-catalog-ids",
                "error",
                "CCB Agent routes or benchmarks reference missing bilingual catalog IDs.",
                references=unresolved_context_ids,
            )
        )
    add_coverage_regression(
        findings,
        "agent-context-catalog-id-mapping",
        context_catalog_resolved,
        context_catalog_references,
        unresolved_references=unresolved_context_ids,
    )
    catalog_by_url = {
        catalog_page_url(catalog, page): page for page in catalog_by_key.values()
    }
    inventory_by_stable = {
        document.get("stable_document_id"): document
        for document in valid_documents
        if isinstance(document.get("stable_document_id"), str)
    }
    inventory_target_by_stable = {
        stable_id: document.get("merge_target") or stable_id
        for stable_id, document in inventory_by_stable.items()
    }
    unresolved_registry_ids: list[dict[str, str]] = []
    registry_catalog_references = 0
    registry_catalog_resolved = 0
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        for declared_id in entry.get("ccb_docs_ids", []):
            if not isinstance(declared_id, str):
                continue
            registry_catalog_references += 1
            effective_id = inventory_target_by_stable.get(declared_id, declared_id)
            languages = {
                language
                for identity, language in catalog_by_key
                if identity == effective_id
            }
            if {"zh_CN", "en"}.issubset(languages):
                registry_catalog_resolved += 1
            else:
                inventory_document = inventory_by_stable.get(declared_id, {})
                page_at_url = catalog_by_url.get(inventory_document.get("zh_url"))
                unresolved_registry_ids.append(
                    {
                        "path": str(entry.get("path")),
                        "declared_id": declared_id,
                        "effective_id": effective_id,
                        "catalog_id_at_zh_url": (
                            page_at_url.get("id") if page_at_url else None
                        ),
                    }
                )
    if unresolved_registry_ids:
        findings.append(
            finding(
                "documentation-registry-unresolved-catalog-ids",
                "error",
                "CCB registry references do not resolve to bilingual CCB-Docs catalog IDs.",
                references=unresolved_registry_ids,
            )
        )
    add_coverage_regression(
        findings,
        "registry-catalog-id-mapping",
        registry_catalog_resolved,
        registry_catalog_references,
        unresolved_references=unresolved_registry_ids,
    )

    invalid_catalog_migrations: list[dict[str, Any]] = []
    verified_catalog_migrations = 0
    for document in permanent_entries:
        stable_id = document.get("stable_document_id")
        target_id = document.get("merge_target") or stable_id
        language_pages = {
            language: catalog_by_key.get((target_id, language))
            for language in ("zh_CN", "en")
        }
        expected_urls = {
            "zh_CN": document.get("zh_url"),
            "en": document.get("en_url"),
        }
        pages_at_expected_urls = {
            language: catalog_by_url.get(url) for language, url in expected_urls.items()
        }
        actual_urls = {
            language: catalog_page_url(catalog, page)
            if page
            else (
                catalog_page_url(catalog, pages_at_expected_urls[language])
                if pages_at_expected_urls[language]
                else None
            )
            for language, page in language_pages.items()
        }
        actual_ids = {
            language: (
                page.get("id")
                if page
                else (
                    pages_at_expected_urls[language].get("id")
                    if pages_at_expected_urls[language]
                    else None
                )
            )
            for language, page in language_pages.items()
        }
        problems: list[str] = []
        for language in ("zh_CN", "en"):
            if language_pages[language] is None:
                if pages_at_expected_urls[language]:
                    problems.append(
                        f"{language} catalog ID is {actual_ids[language]!r}, "
                        f"expected {target_id!r}"
                    )
                else:
                    problems.append(f"missing {language} catalog page and URL")
            elif expected_urls[language] != actual_urls[language]:
                problems.append(f"{language} URL mismatch")
        if problems:
            invalid_catalog_migrations.append(
                {
                    "path": document.get("original_path"),
                    "stable_document_id": stable_id,
                    "target_document_id": target_id,
                    "problems": problems,
                    "expected_urls": expected_urls,
                    "actual_urls": actual_urls,
                    "actual_document_ids": actual_ids,
                }
            )
        else:
            verified_catalog_migrations += 1
    if invalid_catalog_migrations:
        findings.append(
            finding(
                "migration-catalog-url-mismatch",
                "error",
                "Frozen migration IDs or URLs do not match the CCB-Docs catalog.",
                count=len(invalid_catalog_migrations),
                migrations=invalid_catalog_migrations,
            )
        )
    add_coverage_regression(
        findings,
        "migration-catalog-url-mapping",
        verified_catalog_migrations,
        len(permanent_entries),
        invalid_paths=[item["path"] for item in invalid_catalog_migrations],
    )

    return findings, {
        "source_reconciliation": "observed",
        "source_target_ref": target_ref,
        "source_target_commit": source_commit,
        "tracked_markdown": len(tracked_markdown),
        "registered_tracked_markdown": registered_markdown,
        "registry_markdown_coverage_percent": percentage(
            registered_markdown, len(tracked_markdown)
        ),
        "documentation_registry_entries": len(entries),
        "documentation_registry_declared_entries": declared_entry_count,
        "frozen_inventory_expected": 175,
        "frozen_inventory_documents": len(documents),
        "frozen_inventory_terminal_documents": len(terminal_documents),
        "permanent_stub_expected": len(permanent_entries),
        "permanent_stub_verified": verified_stubs,
        "permanent_stub_coverage_percent": percentage(
            verified_stubs, len(permanent_entries)
        ),
        "registry_catalog_references": registry_catalog_references,
        "registry_catalog_references_resolved": registry_catalog_resolved,
        "registry_catalog_coverage_percent": percentage(
            registry_catalog_resolved, registry_catalog_references
        ),
        "agent_context_catalog_references": context_catalog_references,
        "agent_context_catalog_references_resolved": context_catalog_resolved,
        "agent_context_catalog_coverage_percent": percentage(
            context_catalog_resolved, context_catalog_references
        ),
        "migration_catalog_mappings_expected": len(permanent_entries),
        "migration_catalog_mappings_verified": verified_catalog_migrations,
        "migration_catalog_coverage_percent": percentage(
            verified_catalog_migrations, len(permanent_entries)
        ),
        "new_unregistered_markdown": len(unregistered_markdown),
    }


def docs_coverage(
    today: date,
    source_repo: Path | None = None,
    target_ref: str = "HEAD",
) -> dict:
    catalog = load_catalog()
    pages = catalog["pages"]
    findings: list[dict] = []
    debts = translation_debts(catalog, today)
    for debt in debts:
        if debt.overdue:
            findings.append(
                finding(
                    f"translation-overdue:{debt.id}",
                    "error",
                    f"English translation is {debt.age_days} days stale.",
                    stale_since=debt.stale_since,
                    risk_group=debt.risk_group,
                )
            )
    seen_review_ids: set[str] = set()
    for page in pages:
        if page["status"] == "stale":
            findings.append(
                finding(
                    f"stale:{page['id']}:{page['language']}",
                    "warning",
                    page.get("stale_reason") or "Active documentation is marked stale.",
                )
            )
        if page["status"] not in {"active", "stale"} or page["id"] in seen_review_ids:
            continue
        seen_review_ids.add(page["id"])
        next_review = date.fromisoformat(page["verified_at"]) + timedelta(
            days=page["review_interval_days"]
        )
        if today > next_review:
            findings.append(
                finding(
                    f"review-overdue:{page['id']}",
                    "warning",
                    f"Human/source review target passed on {next_review.isoformat()}.",
                    last_human_reviewer=page["last_human_reviewer"],
                )
            )
    ids = {page["id"] for page in pages}
    statuses = Counter(page["status"] for page in pages)
    languages = Counter(page["language"] for page in pages)
    doc_types = Counter(page["doc_type"] for page in pages)
    indexed = sum(page["include_in_ai_index"] for page in pages)
    searchable = sum(page["include_in_search"] for page in pages)
    source_summary: dict[str, Any] = {"source_reconciliation": "not-requested"}
    if source_repo is not None:
        source_findings, source_summary = source_documentation_coverage(
            source_repo,
            target_ref,
            catalog,
        )
        findings.extend(source_findings)
    return report(
        "docs-coverage",
        findings,
        {
            "date": today.isoformat(),
            "stable_document_ids": len(ids),
            "language_pages": len(pages),
            "statuses": dict(sorted(statuses.items())),
            "languages": dict(sorted(languages.items())),
            "doc_types": dict(sorted(doc_types.items())),
            "translation_debts": len(debts),
            "overdue_translation_debts": sum(debt.overdue for debt in debts),
            "searchable_pages": searchable,
            "ai_indexed_pages": indexed,
            **source_summary,
        },
    )


def git(repository: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repository), *args],
        check=check,
        capture_output=True,
    )


def git_text(repository: Path, *args: str) -> str:
    return git(repository, *args).stdout.decode("utf-8").strip()


def git_blob(repository: Path, target_ref: str, path: str) -> bytes | None:
    result = git(repository, "show", f"{target_ref}:{path}", check=False)
    return result.stdout if result.returncode == 0 else None


def contract_fingerprint(repository: Path, target_ref: str, paths: list[str]) -> str | None:
    digest = hashlib.sha256()
    for path in paths:
        content = git_blob(repository, target_ref, path)
        if content is None:
            return None
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(content)
        digest.update(b"\0")
    return digest.hexdigest()


def api_diff(
    source_repo: Path,
    target_ref: str,
    watch_path: Path,
    baseline_path: Path,
) -> dict:
    watch = load_yaml(watch_path)
    baseline = load_yaml(baseline_path)
    if watch.get("schema_version") != 1 or baseline.get("schema_version") != 1:
        raise MaintenanceError("API watch and baseline must use schema_version 1")
    target_commit = git_text(source_repo, "rev-parse", target_ref)
    watched = watch.get("contracts", {})
    baselines = baseline.get("contracts", {})
    if not isinstance(watched, dict) or not isinstance(baselines, dict):
        raise MaintenanceError("API watch and baseline contracts must be mappings")
    findings: list[dict] = []
    contracts: dict[str, dict[str, Any]] = {}
    for identity, spec in watched.items():
        if not isinstance(spec, dict):
            raise MaintenanceError(f"watched contract {identity} must be a mapping")
        paths = spec.get("paths", [])
        if not isinstance(paths, list) or not paths or not all(
            isinstance(path, str) and path for path in paths
        ):
            raise MaintenanceError(f"watched contract {identity} needs non-empty paths")
        missing = [path for path in paths if git_blob(source_repo, target_ref, path) is None]
        expected = baselines.get(identity)
        if expected is not None and not (
            isinstance(expected, str) and len(expected) == 64
        ):
            raise MaintenanceError(
                f"baseline for {identity} must be null or a SHA-256 fingerprint"
            )
        if missing:
            contracts[identity] = {
                "status": "pending-source-contract",
                "paths": paths,
                "missing_paths": missing,
                "fingerprint": None,
                "baseline": expected,
                "pending_source_pr": spec.get("pending_source_pr"),
            }
            if not spec.get("pending_source_pr"):
                findings.append(
                    finding(
                        f"source-contract-missing:{identity}",
                        "warning",
                        "Watched contract paths are not yet present on the source default branch.",
                        missing_paths=missing,
                    )
                )
            continue
        actual = contract_fingerprint(source_repo, target_ref, paths)
        if expected is None:
            state = "baseline-missing"
            findings.append(
                finding(
                    f"baseline-missing:{identity}",
                    "warning",
                    "Contract exists but no Responsible-human-approved baseline is recorded.",
                    fingerprint=actual,
                    target_commit=target_commit,
                )
            )
        elif actual != expected:
            state = "changed"
            findings.append(
                finding(
                    f"api-drift:{identity}",
                    "error",
                    "API contract fingerprint differs from the approved baseline.",
                    expected=expected,
                    actual=actual,
                    target_commit=target_commit,
                )
            )
        else:
            state = "unchanged"
        contracts[identity] = {
            "status": state,
            "paths": paths,
            "missing_paths": [],
            "fingerprint": actual,
            "baseline": expected,
            "pending_source_pr": spec.get("pending_source_pr"),
        }
    return report(
        "api-diff",
        findings,
        {
            "target_ref": target_ref,
            "target_commit": target_commit,
            "contracts": contracts,
            "baseline_source_commit": baseline.get("source_commit"),
        },
    )


def path_exists(repository: Path, target_ref: str, path: str) -> bool:
    return git(repository, "cat-file", "-e", f"{target_ref}:{path}", check=False).returncode == 0


def run_authoritative_agent_benchmark(source_repo: Path) -> tuple[dict | None, dict | None]:
    relative_tool = Path("tools/agent/benchmark_context_pack.py")
    relative_report = Path("ai/agent-benchmark-baseline.json")
    tool = source_repo / relative_tool
    baseline = source_repo / relative_report
    command = [sys.executable, str(tool), "--check", "--output", str(baseline)]
    if not tool.is_file() or not baseline.is_file():
        return None, finding(
            "authoritative-agent-benchmark-missing",
            "blocker",
            "CCB master does not yet contain the context-pack benchmark and baseline.",
            command="python3 tools/agent/benchmark_context_pack.py --check",
            missing=[
                str(path)
                for path in (relative_tool, relative_report)
                if not (source_repo / path).is_file()
            ],
        )
    result = subprocess.run(
        command,
        cwd=source_repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        output = (result.stdout + "\n" + result.stderr).strip()[-2000:]
        return None, finding(
            "authoritative-agent-benchmark-failed",
            "error",
            "CCB context-pack benchmark did not match its checked-in baseline.",
            command="python3 tools/agent/benchmark_context_pack.py --check",
            returncode=result.returncode,
            output=output,
        )
    observations = load_json(baseline)
    return observations, None


def agent_benchmark_readiness(
    source_repo: Path,
    target_ref: str,
    config_path: Path,
    observations_path: Path | None,
    run_source_benchmark: bool = False,
) -> dict:
    config = load_yaml(config_path)
    catalog = load_catalog()
    known_docs = {page["id"] for page in catalog["pages"]}
    target_commit = git_text(source_repo, "rev-parse", target_ref)
    findings: list[dict] = []
    tasks: list[dict] = []
    source_hits = 0
    source_total = 0
    doc_hits = 0
    doc_total = 0
    for task in config.get("tasks", []):
        paths = task.get("expected_paths", [])
        docs = task.get("expected_document_ids", [])
        missing_paths = [
            path for path in paths if not path_exists(source_repo, target_ref, path)
        ]
        missing_docs = [identity for identity in docs if identity not in known_docs]
        source_hits += len(paths) - len(missing_paths)
        source_total += len(paths)
        doc_hits += len(docs) - len(missing_docs)
        doc_total += len(docs)
        if missing_paths or missing_docs:
            findings.append(
                finding(
                    f"benchmark-readiness:{task['id']}",
                    "warning",
                    "Benchmark task lacks required source or documentation context.",
                    missing_paths=missing_paths,
                    missing_document_ids=missing_docs,
                )
            )
        tasks.append(
            {
                "id": task["id"],
                "expected_paths": paths,
                "expected_document_ids": docs,
                "missing_paths": missing_paths,
                "missing_document_ids": missing_docs,
            }
        )
    observations = None
    benchmark_finding = None
    if run_source_benchmark:
        observations, benchmark_finding = run_authoritative_agent_benchmark(source_repo)
    elif observations_path:
        observations = load_json(observations_path)
    if benchmark_finding:
        findings.append(benchmark_finding)
    if observations is None:
        findings.append(
            finding(
                "agent-observations-missing",
                "blocker",
                "No human/model-run observation bundle was supplied; "
                "behavioral metrics remain null.",
            )
        )
    required_metrics = config.get("observation_schema", {}).get("required_metrics", [])
    metrics = {metric: None for metric in required_metrics}
    if observations is not None:
        supplied = observations.get("metrics", {})
        if not isinstance(supplied, dict):
            raise MaintenanceError("agent observation metrics must be an object")
        missing_metrics = [metric for metric in required_metrics if metric not in supplied]
        if missing_metrics:
            findings.append(
                finding(
                    "agent-observations-incomplete",
                    "error",
                    "Agent observation bundle omits required metrics.",
                    missing_metrics=missing_metrics,
                )
            )
        for metric in required_metrics:
            metrics[metric] = supplied.get(metric)
    return report(
        "agent-benchmark",
        findings,
        {
            "target_ref": target_ref,
            "target_commit": target_commit,
            "token_limit": config.get("token_limit"),
            "tasks": tasks,
            "readiness": {
                "source_path_hits": source_hits,
                "source_path_total": source_total,
                "source_path_hit_rate": (
                    round(100 * source_hits / source_total, 2) if source_total else None
                ),
                "document_id_hits": doc_hits,
                "document_id_total": doc_total,
                "document_id_hit_rate": (
                    round(100 * doc_hits / doc_total, 2) if doc_total else None
                ),
            },
            "behavioral_metrics": metrics,
            "observations_supplied": observations is not None,
        },
        status="blocked" if observations is None else None,
    )


def github_api_get(
    endpoint: str,
    token: str,
    api_base: str = "https://api.github.com",
) -> dict[str, Any]:
    """Perform one authenticated, read-only GitHub REST request."""
    url = api_base.rstrip("/") + "/" + endpoint.lstrip("/")
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ccb-docs-permissions-audit",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            body = response.read()
            data = json.loads(body.decode("utf-8")) if body else None
            return {
                "state": "observed",
                "http_status": response.status,
                "data": data,
            }
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")[-1000:]
        try:
            parsed = json.loads(body) if body else {}
            message = parsed.get("message", body) if isinstance(parsed, dict) else body
        except json.JSONDecodeError:
            message = body
        return {
            "state": "unobserved",
            "http_status": error.code,
            "error": message or error.reason,
        }
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        return {
            "state": "unobserved",
            "http_status": None,
            "error": str(error),
        }


def observe_github_permissions(
    repository: str,
    organization: str,
    token: str,
    api_base: str,
) -> tuple[dict[str, Any], list[dict]]:
    """Observe repository and organization controls without mutating GitHub."""
    if repository.count("/") != 1:
        return (
            {
                "state": "unobserved",
                "repository": repository,
                "controls": {},
                "reason": "invalid repository name",
            },
            [
                finding(
                    "github-observation-repository-invalid",
                    "blocker",
                    "Maintenance repository must use the owner/name form.",
                    repository=repository,
                )
            ],
        )
    encoded_repository = "/".join(
        urllib.parse.quote(part, safe="") for part in repository.split("/")
    )
    endpoints = {
        "rulesets": f"repos/{encoded_repository}/rulesets?includes_parents=true",
        "workflow_permissions": f"repos/{encoded_repository}/actions/permissions/workflow",
        "pages": f"repos/{encoded_repository}/pages",
        "pages_environment": f"repos/{encoded_repository}/environments/github-pages",
        "repository_security": f"repos/{encoded_repository}",
        "dependabot_alerts": f"repos/{encoded_repository}/vulnerability-alerts",
        "dependabot_security_updates": (
            f"repos/{encoded_repository}/automated-security-fixes"
        ),
        "organization_2fa": f"orgs/{urllib.parse.quote(organization, safe='')}",
    }
    findings: list[dict] = []
    raw: dict[str, dict[str, Any]] = {}
    controls: dict[str, dict[str, Any]] = {}
    for control, endpoint in endpoints.items():
        observation = github_api_get(endpoint, token, api_base)
        raw[control] = observation
        if observation.get("state") != "observed":
            controls[control] = {
                "state": "unobserved",
                "http_status": observation.get("http_status"),
                "reason": observation.get("error"),
            }
            findings.append(
                finding(
                    f"github-observation-unavailable:{control}",
                    "blocker",
                    "GitHub did not expose this control to the read-only audit.",
                    endpoint=endpoint,
                    http_status=observation.get("http_status"),
                    reason=observation.get("error"),
                )
            )

    def malformed(control: str, message: str) -> None:
        controls[control] = {"state": "unobserved", "reason": message}
        findings.append(
            finding(
                f"github-observation-malformed:{control}",
                "blocker",
                message,
            )
        )

    if raw["rulesets"].get("state") == "observed":
        rulesets = raw["rulesets"].get("data")
        if not isinstance(rulesets, list):
            malformed("rulesets", "GitHub Rulesets response was not a list.")
        else:
            observed_rulesets = []
            details_complete = True
            for item in rulesets:
                if not isinstance(item, dict):
                    details_complete = False
                    findings.append(
                        finding(
                            "github-observation-malformed:ruleset-list-item",
                            "blocker",
                            "GitHub Rulesets response contained a non-object item.",
                        )
                    )
                    continue
                ruleset_id = item.get("id")
                observed = {
                    "id": ruleset_id,
                    "name": item.get("name"),
                    "target": item.get("target"),
                    "enforcement": item.get("enforcement"),
                    "source_type": item.get("source_type"),
                    "detail_state": "unobserved",
                    "rules": None,
                    "bypass_actors": None,
                    "conditions": None,
                }
                if not isinstance(ruleset_id, int):
                    details_complete = False
                    findings.append(
                        finding(
                            "github-observation-malformed:ruleset-id",
                            "blocker",
                            "GitHub Rulesets response omitted a numeric Ruleset ID.",
                            ruleset_name=item.get("name"),
                        )
                    )
                    observed_rulesets.append(observed)
                    continue
                detail_endpoint = f"repos/{encoded_repository}/rulesets/{ruleset_id}"
                detail_observation = github_api_get(detail_endpoint, token, api_base)
                if detail_observation.get("state") != "observed":
                    details_complete = False
                    findings.append(
                        finding(
                            f"github-observation-unavailable:ruleset-detail-{ruleset_id}",
                            "blocker",
                            "GitHub did not expose this Ruleset's effective rules.",
                            endpoint=detail_endpoint,
                            http_status=detail_observation.get("http_status"),
                            reason=detail_observation.get("error"),
                        )
                    )
                    observed_rulesets.append(observed)
                    continue
                detail = detail_observation.get("data")
                if not isinstance(detail, dict) or not isinstance(detail.get("rules"), list):
                    details_complete = False
                    findings.append(
                        finding(
                            f"github-observation-malformed:ruleset-detail-{ruleset_id}",
                            "blocker",
                            "GitHub Ruleset detail omitted its rules array.",
                        )
                    )
                    observed_rulesets.append(observed)
                    continue
                observed.update(
                    {
                        "detail_state": "observed",
                        "rules": detail["rules"],
                        "bypass_actors": detail.get("bypass_actors"),
                        "conditions": detail.get("conditions"),
                    }
                )
                observed_rulesets.append(observed)
            active = [
                item
                for item in observed_rulesets
                if item["enforcement"] == "active" and item["target"] == "branch"
            ]
            controls["rulesets"] = {
                "state": "observed" if details_complete else "partial",
                "active_count": len(active),
                "rulesets": observed_rulesets,
            }
            if not active:
                findings.append(
                    finding(
                        "github-observed-ruleset-not-active",
                        "blocker",
                        "GitHub reports no active repository or inherited Ruleset.",
                    )
                )

    if raw["workflow_permissions"].get("state") == "observed":
        workflow = raw["workflow_permissions"].get("data")
        required_fields = {"default_workflow_permissions", "can_approve_pull_request_reviews"}
        if not isinstance(workflow, dict) or not required_fields.issubset(workflow):
            malformed(
                "workflow_permissions",
                "GitHub workflow-permissions response omitted required fields.",
            )
        else:
            default_permission = workflow["default_workflow_permissions"]
            actions_pr_toggle = workflow["can_approve_pull_request_reviews"]
            controls["workflow_permissions"] = {
                "state": "observed",
                "default_workflow_permissions": default_permission,
                "actions_pull_request_toggle": actions_pr_toggle,
            }
            if default_permission != "read":
                findings.append(
                    finding(
                        "github-observed-workflow-token-not-read-only",
                        "error",
                        "Default GITHUB_TOKEN permission is not read-only.",
                        observed=default_permission,
                    )
                )
            if actions_pr_toggle is not True:
                findings.append(
                    finding(
                        "github-observed-actions-pr-toggle-disabled",
                        "blocker",
                        "Actions cannot create pull requests under the observed "
                        "repository setting.",
                        observed=actions_pr_toggle,
                    )
                )

    if raw["pages"].get("state") == "observed":
        pages = raw["pages"].get("data")
        if not isinstance(pages, dict) or "build_type" not in pages:
            malformed("pages", "GitHub Pages response omitted build_type.")
        else:
            controls["pages"] = {
                "state": "observed",
                "build_type": pages.get("build_type"),
                "status": pages.get("status"),
                "html_url": pages.get("html_url"),
            }
            if pages.get("build_type") != "workflow":
                findings.append(
                    finding(
                        "github-observed-pages-source-mismatch",
                        "error",
                        "GitHub Pages is not deployed from GitHub Actions.",
                        observed=pages.get("build_type"),
                    )
                )

    if raw["pages_environment"].get("state") == "observed":
        environment = raw["pages_environment"].get("data")
        if not isinstance(environment, dict) or "protection_rules" not in environment:
            malformed(
                "pages_environment",
                "GitHub Pages environment response omitted protection_rules.",
            )
        else:
            protection_rules = environment.get("protection_rules")
            controls["pages_environment"] = {
                "state": "observed",
                "name": environment.get("name"),
                "protection_rule_count": (
                    len(protection_rules) if isinstance(protection_rules, list) else None
                ),
                "deployment_branch_policy": environment.get("deployment_branch_policy"),
            }
            if not isinstance(protection_rules, list):
                malformed(
                    "pages_environment",
                    "GitHub Pages protection_rules was not a list.",
                )

    if raw["repository_security"].get("state") == "observed":
        repository_data = raw["repository_security"].get("data")
        security = (
            repository_data.get("security_and_analysis")
            if isinstance(repository_data, dict)
            else None
        )
        if not isinstance(security, dict):
            malformed(
                "repository_security",
                "GitHub omitted security_and_analysis; token permission may be insufficient.",
            )
        else:
            security_fields = {
                "secret_scanning": "secret_scanning",
                "push_protection": "secret_scanning_push_protection",
                "dependabot_security_updates": "dependabot_security_updates",
            }
            observed_security: dict[str, Any] = {}
            missing_security_fields: list[str] = []
            for report_name, github_name in security_fields.items():
                value = security.get(github_name)
                status = value.get("status") if isinstance(value, dict) else None
                observed_security[report_name] = status
                if status is None:
                    missing_security_fields.append(github_name)
                elif status != "enabled":
                    findings.append(
                        finding(
                            f"github-observed-security-disabled:{report_name}",
                            "blocker",
                            f"GitHub reports {report_name} is not enabled.",
                            observed=status,
                        )
                    )
            controls["repository_security"] = {
                "state": "observed" if not missing_security_fields else "partial",
                **observed_security,
            }
            if missing_security_fields:
                findings.append(
                    finding(
                        "github-observation-security-fields-missing",
                        "blocker",
                        "GitHub security response omitted requested controls.",
                        fields=missing_security_fields,
                    )
                )

    for control in ("dependabot_alerts", "dependabot_security_updates"):
        if raw[control].get("state") == "observed":
            controls[control] = {
                "state": "observed",
                "enabled": raw[control].get("http_status") in {200, 204},
                "http_status": raw[control].get("http_status"),
            }

    if raw["organization_2fa"].get("state") == "observed":
        organization_data = raw["organization_2fa"].get("data")
        if not isinstance(organization_data, dict) or (
            "two_factor_requirement_enabled" not in organization_data
        ):
            malformed(
                "organization_2fa",
                "GitHub organization response omitted two_factor_requirement_enabled; "
                "owner permission may be required.",
            )
        else:
            enabled = organization_data["two_factor_requirement_enabled"]
            controls["organization_2fa"] = {
                "state": "observed",
                "enabled": enabled,
            }
            if enabled is not True:
                findings.append(
                    finding(
                        "github-observed-organization-2fa-disabled",
                        "blocker",
                        "GitHub reports organization 2FA enforcement is not enabled.",
                    )
                )

    state = "observed" if all(
        control.get("state") == "observed" for control in controls.values()
    ) and len(controls) == len(endpoints) else "partial"
    return {
        "state": state,
        "repository": repository,
        "organization": organization,
        "api_base": api_base,
        "controls": controls,
    }, findings


def ruleset_policy_findings(observed: dict, desired: dict) -> list[dict]:
    """Compare one fully observed active branch Ruleset with the target policy."""
    findings: list[dict] = []
    raw_rules = observed.get("rules")
    if observed.get("detail_state") != "observed" or not isinstance(raw_rules, list):
        return [
            finding(
                "github-observed-target-ruleset-detail-unavailable",
                "blocker",
                "The target Ruleset is active but its effective rules are unobserved.",
                ruleset_id=observed.get("id"),
            )
        ]
    rules_by_type: dict[str, list[dict]] = {}
    for rule in raw_rules:
        if not isinstance(rule, dict) or not isinstance(rule.get("type"), str):
            findings.append(
                finding(
                    "github-observed-target-ruleset-rule-malformed",
                    "blocker",
                    "The target Ruleset contains a rule without a string type.",
                    ruleset_id=observed.get("id"),
                )
            )
            continue
        rules_by_type.setdefault(rule["type"], []).append(rule)

    def require_rule(rule_type: str, policy_name: str) -> dict | None:
        matches = rules_by_type.get(rule_type, [])
        if len(matches) != 1:
            findings.append(
                finding(
                    f"github-observed-ruleset-policy:{policy_name}",
                    "blocker",
                    f"The target Ruleset needs exactly one {rule_type!r} rule.",
                    observed_count=len(matches),
                )
            )
            return None
        return matches[0]

    pull_request_rule = None
    if desired.get("require_pull_request") is True:
        pull_request_rule = require_rule("pull_request", "pull-request-required")
    if pull_request_rule is not None:
        parameters = pull_request_rule.get("parameters")
        if not isinstance(parameters, dict):
            parameters = {}
        required_approvals = desired.get("required_non_author_human_approvals")
        if isinstance(required_approvals, int):
            observed_approvals = parameters.get("required_approving_review_count")
            if not isinstance(observed_approvals, int) or (
                observed_approvals < required_approvals
            ):
                findings.append(
                    finding(
                        "github-observed-ruleset-policy:approval-count",
                        "blocker",
                        "The target Ruleset does not require the declared approval count.",
                        expected_minimum=required_approvals,
                        observed=observed_approvals,
                    )
                )
        boolean_parameters = {
            "dismiss_stale_reviews": "dismiss_stale_reviews_on_push",
            "require_conversation_resolution": "required_review_thread_resolution",
        }
        for desired_name, github_name in boolean_parameters.items():
            if desired.get(desired_name) is True and parameters.get(github_name) is not True:
                findings.append(
                    finding(
                        f"github-observed-ruleset-policy:{desired_name}",
                        "blocker",
                        f"The target Ruleset does not enforce {desired_name}.",
                        observed=parameters.get(github_name),
                    )
                )

    expected_checks = desired.get("required_status_checks", [])
    if expected_checks:
        status_rule = require_rule("required_status_checks", "required-status-checks")
        parameters = status_rule.get("parameters", {}) if status_rule else {}
        observed_checks = parameters.get("required_status_checks", [])
        observed_contexts = {
            item.get("context")
            for item in observed_checks
            if isinstance(item, dict) and isinstance(item.get("context"), str)
        }
        missing_checks = sorted(set(expected_checks) - observed_contexts)
        if missing_checks:
            findings.append(
                finding(
                    "github-observed-ruleset-policy:status-check-contexts",
                    "blocker",
                    "The target Ruleset omits declared required status checks.",
                    missing=missing_checks,
                    observed=sorted(observed_contexts),
                )
            )

    if desired.get("prohibit_force_push") is True:
        require_rule("non_fast_forward", "force-push-prohibited")
    if desired.get("prohibit_branch_deletion") is True:
        require_rule("deletion", "branch-deletion-prohibited")

    bypass_policy = desired.get("bypass", {})
    bypass_actors = observed.get("bypass_actors")
    if isinstance(bypass_policy, dict) and bypass_policy.get("policy") == "emergency_only":
        if not isinstance(bypass_actors, list):
            findings.append(
                finding(
                    "github-observed-ruleset-policy:bypass-unobserved",
                    "blocker",
                    "The target Ruleset's bypass actors are not observable.",
                )
            )
        elif not bypass_actors:
            findings.append(
                finding(
                    "github-observed-ruleset-policy:emergency-bypass-missing",
                    "blocker",
                    "An active target Ruleset has no recorded emergency bypass actor.",
                )
            )
        elif any(
            not isinstance(actor, dict)
            or actor.get("bypass_mode") not in {"always", "pull_request"}
            for actor in bypass_actors
        ):
            findings.append(
                finding(
                    "github-observed-ruleset-policy:bypass-mode-invalid",
                    "blocker",
                    "The target Ruleset contains an unrecognized bypass mode.",
                )
            )
    return findings


def permissions_audit(
    settings_path: Path,
    maintenance_path: Path,
    github_token: str | None = None,
    github_api_base: str | None = None,
    github_repository: str | None = None,
    github_organization: str | None = None,
) -> dict:
    settings = load_yaml(settings_path)
    maintenance = load_yaml(maintenance_path)
    record = settings.get("manual_record", {})
    target = settings.get("target", {})
    blockers = maintenance.get("governance_blockers", {})
    findings: list[dict] = []
    reviewers = record.get("confirmed_reviewers", [])
    minimum = settings.get("prerequisites", {}).get("minimum_confirmed_human_reviewers", 2)
    if len(reviewers) < minimum:
        issue = blockers.get("required_human_reviewers", {}).get("issue")
        findings.append(
            finding(
                "confirmed-reviewers",
                "blocker",
                f"{len(reviewers)} confirmed reviewers; {minimum} required before enforcement.",
                issue=issue,
            )
        )
    ruleset_enabled = (
        settings.get("enforcement") == "active"
        and record.get("protection_enabled_at") is not None
    )
    if not ruleset_enabled:
        findings.append(
            finding(
                "ruleset-not-enforced",
                "blocker",
                "Ruleset remains target-only to avoid locking the repository.",
                issue=blockers.get("ruleset_enforcement", {}).get("issue"),
            )
        )
    if record.get("actions_pr_creation_result") != "enabled":
        findings.append(
            finding(
                "actions-pr-creation",
                "blocker",
                "Organization policy still blocks Actions pull-request creation.",
                issue=blockers.get("actions_pull_request_creation", {}).get("issue"),
            )
        )
    two_factor_state = blockers.get("organization_2fa", {}).get("state")
    if two_factor_state != "enabled_after_audit":
        findings.append(
            finding(
                "organization-2fa",
                "blocker",
                "Organization 2FA enforcement awaits member audit, notice, and owner action.",
                issue=blockers.get("organization_2fa", {}).get("issue"),
            )
        )
    required_checks = record.get("required_checks", [])
    checks_verified = bool(required_checks) and record.get("required_checks_verified_at")
    token = os.environ.get("GITHUB_TOKEN") if github_token is None else github_token
    repository = github_repository or maintenance.get("repository")
    inferred_organization = (
        repository.split("/", 1)[0]
        if isinstance(repository, str) and "/" in repository
        else None
    )
    organization = github_organization or inferred_organization
    api_base = github_api_base or os.environ.get("GITHUB_API_URL", "https://api.github.com")
    if not token:
        github_observations = {
            "state": "unobserved",
            "repository": repository,
            "organization": organization,
            "api_base": api_base,
            "controls": {},
            "reason": "GITHUB_TOKEN is missing",
        }
        findings.append(
            finding(
                "github-observation-token-missing",
                "blocker",
                "GITHUB_TOKEN is missing; live repository and organization controls "
                "are unobserved.",
            )
        )
    elif not isinstance(repository, str):
        github_observations = {
            "state": "unobserved",
            "repository": repository,
            "organization": organization,
            "api_base": api_base,
            "controls": {},
            "reason": "maintenance repository is missing",
        }
        findings.append(
            finding(
                "github-observation-repository-missing",
                "blocker",
                "Maintenance configuration omits the GitHub repository name.",
            )
        )
    elif not isinstance(organization, str) or not organization:
        github_observations = {
            "state": "unobserved",
            "repository": repository,
            "organization": organization,
            "api_base": api_base,
            "controls": {},
            "reason": "GitHub organization is missing",
        }
        findings.append(
            finding(
                "github-observation-organization-missing",
                "blocker",
                "The GitHub organization name cannot be inferred or was not supplied.",
            )
        )
    else:
        github_observations, observation_findings = observe_github_permissions(
            repository,
            organization,
            token,
            api_base,
        )
        findings.extend(observation_findings)

    ruleset_observation = github_observations.get("controls", {}).get("rulesets", {})
    if ruleset_observation.get("state") == "observed":
        active_rulesets = [
            item
            for item in ruleset_observation.get("rulesets", [])
            if item.get("enforcement") == "active" and item.get("target") == "branch"
        ]
        desired_ruleset_name = target.get("ruleset", {}).get("name")
        matching_rulesets = [
            item
            for item in active_rulesets
            if not desired_ruleset_name or item.get("name") == desired_ruleset_name
        ]
        observed_enabled = bool(matching_rulesets)
        ruleset_observation["target_name"] = desired_ruleset_name
        ruleset_observation["target_match_count"] = len(matching_rulesets)
        if active_rulesets and not matching_rulesets:
            findings.append(
                finding(
                    "github-observed-target-ruleset-missing",
                    "blocker",
                    "Active branch Rulesets do not include the declared target Ruleset.",
                    target_name=desired_ruleset_name,
                    active_names=[item.get("name") for item in active_rulesets],
                )
            )
        if len(matching_rulesets) == 1:
            findings.extend(
                ruleset_policy_findings(matching_rulesets[0], target.get("ruleset", {}))
            )
        elif len(matching_rulesets) > 1:
            findings.append(
                finding(
                    "github-observed-target-ruleset-duplicated",
                    "blocker",
                    "More than one active branch Ruleset matches the declared target name.",
                    target_name=desired_ruleset_name,
                    matching_ids=[item.get("id") for item in matching_rulesets],
                )
            )
        if observed_enabled != ruleset_enabled:
            findings.append(
                finding(
                    "github-declaration-drift:rulesets",
                    "warning",
                    "Observed active Rulesets differ from the manual repository-settings record.",
                    observed_active=observed_enabled,
                    declared_active=ruleset_enabled,
                )
            )
    workflow_observation = github_observations.get("controls", {}).get(
        "workflow_permissions", {}
    )
    if workflow_observation.get("state") == "observed":
        observed_actions_pr = workflow_observation.get("actions_pull_request_toggle") is True
        declared_actions_pr = record.get("actions_pr_creation_result") == "enabled"
        if observed_actions_pr != declared_actions_pr:
            findings.append(
                finding(
                    "github-declaration-drift:actions-pr-creation",
                    "warning",
                    "Observed Actions pull-request toggle differs from the manual record.",
                    observed_enabled=observed_actions_pr,
                    declared_enabled=declared_actions_pr,
                )
            )
    two_factor_observation = github_observations.get("controls", {}).get(
        "organization_2fa", {}
    )
    if two_factor_observation.get("state") == "observed":
        observed_two_factor = two_factor_observation.get("enabled") is True
        declared_two_factor = two_factor_state == "enabled_after_audit"
        if observed_two_factor != declared_two_factor:
            findings.append(
                finding(
                    "github-declaration-drift:organization-2fa",
                    "warning",
                    "Observed organization 2FA differs from the declared blocker state.",
                    observed_enabled=observed_two_factor,
                    declared_enabled=declared_two_factor,
                )
            )
    observations_complete = github_observations.get("state") == "observed"
    unsafe_findings = any(
        item.get("severity") in {"blocker", "error"} for item in findings
    )
    return report(
        "permissions-audit",
        findings,
        {
            "enforcement": settings.get("enforcement"),
            "confirmed_reviewers": reviewers,
            "required_checks": required_checks,
            "required_checks_verified_at": record.get("required_checks_verified_at"),
            "target": target,
            "protection_enabled_at": record.get("protection_enabled_at"),
            "blockers": blockers,
            "github_observations": github_observations,
            "safe_to_enable_required_approval": len(reviewers) >= minimum
            and bool(checks_verified)
            and observations_complete
            and not unsafe_findings,
        },
        status="blocked" if findings else "pass",
    )


def archive_review(today: date) -> dict:
    catalog = load_catalog()
    archived = [page for page in catalog["pages"] if page["status"] == "archived"]
    findings: list[dict] = []
    pages_by_id: dict[str, list[dict]] = {}
    for page in archived:
        pages_by_id.setdefault(page["id"], []).append(page)
        if page["include_in_search"] or page["include_in_ai_index"]:
            findings.append(
                finding(
                    f"archive-index-leak:{page['id']}:{page['language']}",
                    "error",
                    "Archived page is admitted to search or AI indexing.",
                )
            )
    for identity, language_pages in sorted(pages_by_id.items()):
        due = min(
            date.fromisoformat(page["verified_at"])
            + timedelta(days=page["review_interval_days"])
            for page in language_pages
        )
        if today > due:
            findings.append(
                finding(
                    f"archive-review-overdue:{identity}",
                    "warning",
                    f"Archive review target passed on {due.isoformat()}.",
                )
            )
    return report(
        "archive-review",
        findings,
        {
            "date": today.isoformat(),
            "archived_document_ids": len({page["id"] for page in archived}),
            "archived_language_pages": len(archived),
            "excluded_from_search": sum(not page["include_in_search"] for page in archived),
            "excluded_from_ai": sum(not page["include_in_ai_index"] for page in archived),
        },
    )


def write_report(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    coverage = subparsers.add_parser("docs-coverage")
    coverage.add_argument("--today", type=date.fromisoformat, default=date.today())
    coverage.add_argument("--source-repo", type=Path, required=True)
    coverage.add_argument("--target-ref", default="HEAD")
    api = subparsers.add_parser("api-diff")
    api.add_argument("--source-repo", type=Path, required=True)
    api.add_argument("--target-ref", default="HEAD")
    api.add_argument("--watch", type=Path, default=ROOT / "config/api-contract-watch.yml")
    api.add_argument(
        "--baseline", type=Path, default=ROOT / "config/api-contract-baseline.yml"
    )
    benchmark = subparsers.add_parser("agent-benchmark")
    benchmark.add_argument("--source-repo", type=Path, required=True)
    benchmark.add_argument("--target-ref", default="HEAD")
    benchmark.add_argument(
        "--config", type=Path, default=ROOT / "config/agent-benchmark.yml"
    )
    benchmark.add_argument("--observations", type=Path)
    benchmark.add_argument("--run-source-benchmark", action="store_true")
    permissions = subparsers.add_parser("permissions")
    permissions.add_argument(
        "--settings", type=Path, default=ROOT / "repository-settings.target.yml"
    )
    permissions.add_argument(
        "--maintenance", type=Path, default=ROOT / "config/maintenance.yml"
    )
    permissions.add_argument("--github-repository")
    permissions.add_argument("--github-organization")
    permissions.add_argument("--github-token-env", default="GITHUB_TOKEN")
    archive = subparsers.add_parser("archive")
    archive.add_argument("--today", type=date.fromisoformat, default=date.today())
    for subparser in (coverage, api, benchmark, permissions, archive):
        subparser.add_argument("--json-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "docs-coverage":
            payload = docs_coverage(
                args.today,
                args.source_repo.resolve(),
                args.target_ref,
            )
        elif args.command == "api-diff":
            payload = api_diff(
                args.source_repo.resolve(), args.target_ref, args.watch, args.baseline
            )
        elif args.command == "agent-benchmark":
            payload = agent_benchmark_readiness(
                args.source_repo.resolve(),
                args.target_ref,
                args.config,
                args.observations,
                args.run_source_benchmark,
            )
        elif args.command == "permissions":
            payload = permissions_audit(
                args.settings,
                args.maintenance,
                github_token=os.environ.get(args.github_token_env, ""),
                github_repository=args.github_repository,
                github_organization=args.github_organization,
            )
        else:
            payload = archive_review(args.today)
        write_report(args.json_output, payload)
    except (
        CatalogError,
        MaintenanceError,
        OSError,
        ValueError,
        KeyError,
        subprocess.CalledProcessError,
        yaml.YAMLError,
        json.JSONDecodeError,
    ) as error:
        print(error, file=sys.stderr)
        return 1
    print(
        f"generated {payload['kind']} report: {payload['status']}, "
        f"{len(payload['findings'])} findings"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
