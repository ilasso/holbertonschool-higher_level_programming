#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsonbody = JSON.parse(body);
  const chars = jsonbody.results[0].characters;

  for (let i = 0; i < chars.length; i++) {
    if (chars[i].includes('/18/')) {
      request(chars[i], function (error2, response2, body2) {
        console.log(JSON.parse(body2).films.length);
      });
    }
  }
});
