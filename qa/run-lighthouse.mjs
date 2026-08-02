import { mkdir, writeFile } from "node:fs/promises";

import { chromium } from "@playwright/test";
import { launch } from "chrome-launcher";
import lighthouse from "lighthouse";

import { startSiteServer } from "./serve.mjs";

const thresholds = {
  accessibility: 0.98,
  "best-practices": 0.95,
  performance: 0.80,
  seo: 0.90,
};
const routes = ["/CCB-Docs/", "/CCB-Docs/en/architecture/project-map/"];

await mkdir("artifacts/lighthouse", { recursive: true });
const server = await startSiteServer(0);
const serverAddress = server.address();
const browser = await launch({
  chromePath: chromium.executablePath(),
  chromeFlags: ["--headless", "--no-sandbox", "--disable-gpu"],
});

let failed = false;
try {
  for (const [index, route] of routes.entries()) {
    const url = `http://127.0.0.1:${serverAddress.port}${route}`;
    const result = await lighthouse(url, {
      logLevel: "error",
      output: "json",
      port: browser.port,
      onlyCategories: Object.keys(thresholds),
    });
    if (!result) {
      throw new Error(`Lighthouse returned no result for ${url}`);
    }
    await writeFile(
      `artifacts/lighthouse/report-${index + 1}.json`,
      result.report,
      "utf8",
    );
    const scores = Object.fromEntries(
      Object.entries(result.lhr.categories).map(([name, value]) => [name, value.score]),
    );
    process.stdout.write(`${url} ${JSON.stringify(scores)}\n`);
    for (const [category, minimum] of Object.entries(thresholds)) {
      if ((scores[category] ?? 0) < minimum) {
        process.stderr.write(
          `${url}: ${category} score ${scores[category]} is below ${minimum}\n`,
        );
        failed = true;
      }
    }
  }
} finally {
  await browser.kill();
  await new Promise((resolve, reject) => {
    server.close((error) => (error ? reject(error) : resolve()));
  });
}

if (failed) {
  process.exitCode = 1;
}
