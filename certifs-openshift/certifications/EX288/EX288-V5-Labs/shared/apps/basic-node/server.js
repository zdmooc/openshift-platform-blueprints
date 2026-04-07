const http = require('http');
const fs = require('fs');

const port = process.env.PORT || 8080;
const message = process.env.APP_MESSAGE || 'hello from basic-node';
const secretPath = process.env.SECRET_FILE || '/opt/app-root/src/secret/token';

const server = http.createServer((req, res) => {
  if (req.url === '/healthz') {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    return res.end('ok');
  }
  if (req.url === '/readyz') {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    return res.end('ready');
  }
  if (req.url === '/secret') {
    try {
      const content = fs.readFileSync(secretPath, 'utf8').trim();
      res.writeHead(200, {'Content-Type': 'text/plain'});
      return res.end(content);
    } catch (err) {
      res.writeHead(500, {'Content-Type': 'text/plain'});
      return res.end('secret unavailable');
    }
  }
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end(message);
});

server.listen(port, () => {
  console.log(`Listening on ${port}`);
});
