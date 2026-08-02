import AxeBuilder from "@axe-core/playwright";
import { expect, test } from "@playwright/test";

test("each language exposes canonical metadata and same-page switching", async ({ page }) => {
  await page.goto("architecture/project-map/");
  await expect(page.locator('link[rel="canonical"]')).toHaveAttribute(
    "href",
    "https://crimsoncrossbunker.github.io/CCB-Docs/architecture/project-map/",
  );
  await expect(page.locator('link[hreflang="en"]')).toHaveAttribute(
    "href",
    "https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/project-map/",
  );
  await expect(page.locator(".ccb-page-provenance")).toContainText("commit");
  await expect(page.locator('[data-ccb-issue-link]')).toBeVisible();
  const structured = await page.locator('script[type="application/ld+json"]').textContent();
  expect(JSON.parse(structured)["@type"]).toBe("TechArticle");
});

test("Alt+L follows the matching English page", async ({ page }) => {
  await page.goto("architecture/project-map/");
  await page.keyboard.press("Alt+l");
  await expect(page).toHaveURL(/\/CCB-Docs\/en\/architecture\/project-map\/$/);
});

test("Chinese and English search return the expected page", async ({ page }) => {
  const cases = [
    ["", "项目地图", "项目地图"],
    ["en/", "project map", "Project map"],
  ];
  for (const [route, query, expected] of cases) {
    await page.goto(`${route}?q=${encodeURIComponent(query)}`);
    const input = page.locator('input[data-md-component="search-query"]');
    await expect(input).toHaveValue(query);
    await expect(page.locator(".md-search-result__link").first()).toContainText(expected);
  }
});

test("representative pages have no axe violations", async ({ page }) => {
  for (const route of ["", "en/architecture/project-map/"]) {
    await page.goto(route);
    const results = await new AxeBuilder({ page }).analyze();
    expect(results.violations).toEqual([]);
  }
});

test("404 page resolves a catalog migration without an automatic redirect", async ({ page }) => {
  await page.route("**/ai/redirects.json", async (route) => {
    await route.fulfill({
      contentType: "application/json",
      body: JSON.stringify({
        "zh_CN:/old-page.md": "https://crimsoncrossbunker.github.io/CCB-Docs/architecture/project-map/",
      }),
    });
  });
  const response = await page.goto("old-page/");
  expect(response.status()).toBe(404);
  const replacement = page.locator("[data-ccb-migration-result] a");
  await expect(replacement).toBeVisible();
  await expect(replacement).toHaveAttribute(
    "href",
    "https://crimsoncrossbunker.github.io/CCB-Docs/architecture/project-map/",
  );
});

test("desktop bilingual pages match reviewed visual baselines", async ({ page }) => {
  for (const [route, snapshot] of [
    ["", "home-zh.png"],
    ["en/", "home-en.png"],
  ]) {
    await page.goto(route);
    await expect(page).toHaveScreenshot(snapshot, { fullPage: true });
  }
});
