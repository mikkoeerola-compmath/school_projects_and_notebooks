const http = require('http');

http.createServer(function(req, res) {
    res.writeHead(200, { 'content-type' : 'text/html'});
    const headers= req.headers;
    res.write(JSON.stringify(headers));
    res.end();
}).listen(3000);
