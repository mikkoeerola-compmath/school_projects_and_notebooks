const http = require('node:http');
http
  .createServer((request, response) => {
    response.writeHead(200, { "Content-type": "text/plain"});
    let body = '';
    request
      .on('data', chunk => {
        console.log(chunk);
        console.log(chunk.toString());
        body += chunk.toString();
        console.log(body);
      })
      .on('end', () => {
        console.log(body);
        console.log(reverseText(body));
        body = reverseText(body);
        response.end(body);
      });
  }).listen(3000);

function reverseText(string) {
    return string.split('').reverse().join('');
}