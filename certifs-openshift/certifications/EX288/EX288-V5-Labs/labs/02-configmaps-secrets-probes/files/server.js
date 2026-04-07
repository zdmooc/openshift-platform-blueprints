const http = require('http');
const fs = require('fs');
const port = process.env.PORT || 8080;
const secretPath = '/opt/app-root/src/secret/token';

http.createServer((req, res) => {
  if (req.url === '/healthz') return res.end('ok');
  if (req.url === '/readyz') return res.end('ready');
  if (req.url === '/secret') {
    try { return res.end(fs.readFileSync(secretPath, 'utf8')); }
    catch (e) { res.statusCode = 500; return res.end('secret unavailable'); }
  }
  return res.end(process.env.APP_MESSAGE || 'hello');
}).listen(port);
