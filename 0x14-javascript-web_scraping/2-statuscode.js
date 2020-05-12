#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('code:', error);
  }
  console.log('code:', response && response.statusCode);
});
