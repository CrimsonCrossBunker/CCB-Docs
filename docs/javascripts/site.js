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

  const warnLegacyLuaPages = () => {
    if (!window.location.pathname.includes("/api/lua/v5/")) {
      return;
    }
    const article = document.querySelector("article.md-content__inner");
    if (!(article instanceof HTMLElement) || article.querySelector("[data-ccb-lua-v5-warning]")) {
      return;
    }
    const english = window.location.pathname.includes("/CCB-Docs/en/");
    const warning = document.createElement("div");
    warning.className = "ccb-page-banner ccb-page-banner--archived";
    warning.dataset.ccbLuaV5Warning = "";
    const replacement = english
      ? "/CCB-Docs/en/api/lua/v1/overview/"
      : "/CCB-Docs/api/lua/v1/overview/";
    warning.innerHTML = english
      ? `<strong>Removed API:</strong> Lua API v5 is historical and no longer runs in CCB. Use <a href="${replacement}">Lua Platform v1</a>.`
      : `<strong>已移除的 API：</strong>Lua API v5 仅作历史保留，当前 CCB 已无法运行。请使用 <a href="${replacement}">Lua Platform v1</a>。`;
    article.prepend(warning);
  };

  activateKeyboardShortcuts();
  lookupMigration();
  warnLegacyLuaPages();
})();
