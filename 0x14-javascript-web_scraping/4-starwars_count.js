#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsonbody = JSON.parse(body);
  const chars = jsonbody.results;
  let count = 0;
  for (let i = 0; i < chars.length; i++) {
    const movies = chars[i].characters;
    for (let j = 0; j < movies.length; j++) {
      if (movies[j].includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
