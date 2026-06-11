const http = require('http');
const fs = require('fs');
const path = require('path');

module.exports = http.createServer((req, res) => {
    let url = req.url;
    switch (url) {
        case '/classical':
            readFileSendResponse("homer.html", 'text/html', res);
            break;
        case '/dystopy':
            readFileSendResponse("bradbury.html", 'text/html', res);
            break;
        case '/':
            readFileSendResponse("index.html", 'text/html', res);
            break;
        default:
            res.statusCode = 404;
            res.statusMessage = 'Requested content not found';
            res.end();
    }
}).listen(3000);

const readFileSendResponse = (fileName, contentType, response) => {
    fs.readFile(path.resolve(fileName), function (error, file) {
      if (error) {
        response.writeHead(404);
        response.write('An error occured: ', error);
      } else {
        response.writeHead(200, { 'Content-Type': contentType });
        response.write(file);
      }
      response.end();
    });
  }