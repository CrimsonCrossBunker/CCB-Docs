import { createReadStream } from "node:fs";
import { stat } from "node:fs/promises";
import { createServer } from "node:http";
import path from "node:path";
import { pathToFileURL } from "node:url";

const root = path.resolve("site");
const prefix = "/CCB-Docs";
const contentTypes = new Map([
  [".css", "text/css; charset=utf-8"],
  [".html", "text/html; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".jsonl", "application/x-ndjson; charset=utf-8"],
  [".svg", "image/svg+xml"],
  [".txt", "text/plain; charset=utf-8"],
  [".xml", "application/xml; charset=utf-8"],
]);

const safeFile = async (pathname) => {
  let relative = decodeURIComponent(pathname).replace(prefix, "").replace(/^\/+/, "");
  if (!relative || relative.endsWith("/")) {
    relative += "index.html";
  }
  const candidate = path.resolve(root, relative);
  if (candidate !== root && !candidate.startsWith(`${root}${path.sep}`)) {
    return null;
  }
  try {
    const details = await stat(candidate);
    return details.isFile() ? candidate : null;
  } catch (_error) {
    return null;
  }
};

const sendFile = (response, file, statusCode = 200, method = "GET") => {
  response.writeHead(statusCode, {
    "cache-control": "no-store",
    "content-type": contentTypes.get(path.extname(file)) || "application/octet-stream",
  });
  if (method === "HEAD") {
    response.end();
  } else {
    createReadStream(file).pipe(response);
  }
};

export const startSiteServer = async (port = 4173) => {
  const server = createServer(async (request, response) => {
    const url = new URL(request.url || "/", "http://127.0.0.1");
    if (url.pathname === prefix) {
      response.writeHead(308, { location: `${prefix}/` });
      response.end();
      return;
    }
    const file = url.pathname.startsWith(`${prefix}/`)
      ? await safeFile(url.pathname)
      : null;
    if (file) {
      sendFile(response, file, 200, request.method);
      return;
    }
    const language404 = url.pathname.startsWith(`${prefix}/en/`)
      ? path.join(root, "en/404.html")
      : path.join(root, "404.html");
    sendFile(response, language404, 404, request.method);
  });
  await new Promise((resolve) => server.listen(port, "127.0.0.1", resolve));
  return server;
};

const invokedDirectly = process.argv[1]
  && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href;
if (invokedDirectly) {
  const server = await startSiteServer();
  const address = server.address();
  process.stdout.write(`CCB-Docs QA server listening on ${address.port}\n`);
}
