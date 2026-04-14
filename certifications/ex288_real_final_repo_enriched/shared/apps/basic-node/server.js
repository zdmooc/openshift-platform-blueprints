const http = require("http");
const fs = require("fs");

const port = process.env.PORT || 8080;
const message = process.env.APP_MESSAGE || "hello from basic-node";
const token = process.env.APP_TOKEN || "no-token";
const sharedFile = process.env.SHARED_FILE || "/shared/message.txt";

http.createServer((req, res) => {
  if (req.url === "/healthz") return res.end("ok");
  if (req.url === "/readyz") return res.end("ready");
  if (req.url === "/startupz") return res.end("started");
  if (req.url === "/env") return res.end(JSON.stringify({message, token}));
  if (req.url === "/shared") {
    try {
      return res.end(fs.readFileSync(sharedFile, "utf8"));
    } catch (e) {
      res.statusCode = 404;
      return res.end("shared file not found");
    }
  }
  return res.end(message + "\n");
}).listen(port, () => console.log(`listening on ${port}`));
