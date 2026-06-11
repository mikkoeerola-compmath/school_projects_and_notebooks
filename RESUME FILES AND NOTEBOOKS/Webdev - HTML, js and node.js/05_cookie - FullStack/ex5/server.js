// Import the Express module
const express = require('express');
const url = require('url');
const app = express();  // Create an Express application

// TODO: Create a route that responds with "Welcome to my simple Express.js server!" when the user visits "/"
app.get('/', (req, res) => {
  res.send('Welcome to my simple Express.js server!');
});

// TODO: Create a route that responds with "This is the about page." when the user visits "/about"
app.get('/about', (req, res) => {
  res.send("This is the about page.");
});

// TODO: Create a route that responds with JSON data for email and phone when the user visits "/contact"
// The JSON data should have the following format:
// {
//   email: 'contact@myserver.com',
//   phone: '123-456-7890'
// }
app.get('/contact', (req, res) => {
  let contacts = {email: 'contact@myserver.com', phone: '123-456-7890'};
  console.log(contacts);
  res.setHeader('Content-type', 'application/json');
  res.send(JSON.stringify(contacts));
});

// TODO: Create a route that responds with "Hello, username! You are age years old." when the user visits /user/:username with a query parameter age. 
// If such query parameter is not provided, the route should respond with "Hello, username! Age not provided."
app.get('/user/:username', (req, res) => {
  let parsedUrl = url.parse(req.url, true);
  let username = parsedUrl.pathname.substring(6);
  let age = parsedUrl.query.age? parsedUrl.query.age : null;
  if (age === null) res.send(`Hello, ${username}! Age not provided.`);
  else res.send(`Hello, ${username}! You are ${age} years old.`)
});

// DO NOT MODIFY BELOW THIS LINE
// Conditionally start the server if this script is run directly
if (require.main === module) {
  app.listen(3000, () => {
      console.log('Server is running on http://localhost:3000');
  });
}

// For Plussa grader
module.exports = app;