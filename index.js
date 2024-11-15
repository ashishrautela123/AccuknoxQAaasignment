// Import the required modules
const https = require('https');
const fs = require('fs');
const express = require('express');  // or any other framework you're using

const app = express();

// Read the SSL certificate and private key files
const options = {
  key: fs.readFileSync('./wisecow/server.key'),
  cert: fs.readFileSync('./wisecow/server.crt'),
};

// Create routes
app.get('/', (req, res) => {
  res.send('Secure connection over HTTPS!');
});

// Start the HTTPS server (on port 4499)
https.createServer(options, app).listen(4499, () => {
  console.log('Server is running on https://localhost:4499');
});
