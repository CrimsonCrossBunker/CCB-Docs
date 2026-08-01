import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./qa/tests",
  fullyParallel: false,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 1 : 0,
  workers: 1,
  reporter: [
    ["line"],
    ["html", { outputFolder: "artifacts/playwright-report", open: "never" }],
  ],
  expect: {
    timeout: 10_000,
    toHaveScreenshot: {
      animations: "disabled",
      maxDiffPixelRatio: 0.025,
    },
  },
  use: {
    baseURL: "http://127.0.0.1:4173/CCB-Docs/",
    reducedMotion: "reduce",
    trace: "retain-on-failure",
  },
  webServer: {
    command: "node qa/serve.mjs",
    url: "http://127.0.0.1:4173/CCB-Docs/",
    reuseExistingServer: !process.env.CI,
    timeout: 30_000,
  },
  projects: [
    {
      name: "chromium",
      use: {
        ...devices["Desktop Chrome"],
        colorScheme: "light",
        locale: "zh-CN",
      },
    },
  ],
  outputDir: "artifacts/playwright-results",
});
