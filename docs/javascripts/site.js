(() => {
  "use strict";

  const activateKeyboardShortcuts = () => {
    document.addEventListener("keydown", (event) => {
      if (!event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) {
        return;
      }
      const target = event.target;
      if (target instanceof HTMLElement && target.matches("input, textarea, select, [contenteditable]")) {
        return;
      }
      const key = event.key.toLowerCase();
      const selector = key === "l"
        ? "[data-ccb-language-switch]"
        : key === "i"
          ? "[data-ccb-issue-link]"
          : null;
      if (!selector) {
        return;
      }
      const link = document.querySelector(selector);
      if (link instanceof HTMLAnchorElement) {
        event.preventDefault();
        link.click();
      }
    });
  };

  const migrationCandidates = (relativePath) => {
    const normalized = `/${relativePath.replace(/^\/+|\/+$/g, "")}`;
    const candidates = [normalized, `${normalized}.md`];
    if (normalized.endsWith("/index")) {
      candidates.push(`${normalized}.md`);
    }
    return [...new Set(candidates)];
  };

  const lookupMigration = async () => {
    const lookup = document.querySelector("[data-ccb-migration-map]");
    const result = document.querySelector("[data-ccb-migration-result]");
    if (!(lookup instanceof HTMLElement) || !(result instanceof HTMLElement)) {
      return;
    }
    const mapUrl = lookup.dataset.ccbMigrationMap;
    const basePath = lookup.dataset.ccbBasePath || "/CCB-Docs/";
    const language = lookup.dataset.ccbLanguage || "zh_CN";
    if (!mapUrl) {
      return;
    }
    let relative = window.location.pathname;
    const baseIndex = relative.indexOf(basePath);
    if (baseIndex >= 0) {
      relative = relative.slice(baseIndex + basePath.length);
    }
    if (language === "en") {
      relative = relative.replace(/^en\//, "");
    }
    try {
      const response = await fetch(mapUrl, { credentials: "same-origin" });
      if (!response.ok) {
        return;
      }
      const redirects = await response.json();
      const match = migrationCandidates(relative)
        .map((candidate) => redirects[`${language}:${candidate}`])
        .find(Boolean);
      if (match) {
        const link = result.querySelector("a");
        if (link instanceof HTMLAnchorElement) {
          link.href = match;
          result.hidden = false;
          link.focus();
        }
      }
    } catch (_error) {
      // A 404 page remains useful without JavaScript or a network response.
    }
  };

  activateKeyboardShortcuts();
  lookupMigration();
})();
