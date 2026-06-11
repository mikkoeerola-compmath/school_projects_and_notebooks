const http = require('http');
const fs = require('fs');
const path = require('path');

http.createServer((req, res) => {
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
            console.log("but here I was");
            res.end();
    }
}).listen(3000);

const readFileSendResponse = (fileName, contentType, response) => {
    fs.readFile(path.resolve(fileName), function (error, file) {
      if (error) {
        console.log("i was not here");
        response.writeHead(404);
        response.write('An error occured: ', error);
      } else {
        console.log("or here");
        response.writeHead(200, { 'Content-Type': contentType });
        response.write(file);
      }
      response.end();
    });
  }