const http = require('http');
const fs = require('fs');
const path = require('path');

http.createServer(function (request, response) {

  const acceptType = request.headers['accept'];
  
  console.log(request.headers);
  console.log(acceptType);

  switch (acceptType) {
    case 'application/json':
      readFileSendResponse('data.json', acceptType, response);
      break;
    case 'application/zip' :
      readFileSendResponse('data.zip', acceptType, response);
      break;
    case 'application/xml':
      readFileSendResponse('data.xml', acceptType, response);
      break;
    case 'text/html':
      readFileSendResponse('data.html', acceptType, response);
      break;
    case 'text/css':
      readFileSendResponse('data.css', acceptType, response);
      break;
    case 'text/plain':
      readFileSendResponse('data.txt', acceptType, response);
      break;
    case '*/*':
      console.log("i was here");
      readFileSendResponse('data.txt', acceptType, response);
      break;
    default :
      response.statusCode = 406;
      response.statusMessage = 'Content type not available';
      console.log("and here");
      response.end();
  }
}).listen(3000);

/* 
  * @param {string} fileName - name of the file to be read
  * @param {string} contentType - type of the content to be sent in the response
  * @param {object} response - response object
  */
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