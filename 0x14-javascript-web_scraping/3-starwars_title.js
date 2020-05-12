#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + parseInt(process.argv[2]);
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const title = JSON.parse(body);
  console.log(title.title);
});
