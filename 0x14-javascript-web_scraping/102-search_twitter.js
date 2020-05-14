#!/usr/bin/node

const request = require('request');
const utf8 = require('utf8');
const base64 = require('base-64');
const key = base64.encode(utf8.encode(process.argv[2] + ':' + process.argv[3]));

request.post({
  url: 'https://api.twitter.com/oauth2/token',
  headers: {
    Authorization: 'Basic ' + key,
    'content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  qs: { grant_type: 'client_credentials' }
},
function (err, resp, body) {
  if (err) {
    console.log(err);
  }
  const token = JSON.parse(body).access_token;
  request({
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: { Authorization: 'Bearer ' + token },
    qs: { q: process.argv[4], count: 5 }
  }, function (error, response, body2) {
    if (error) {
      console.log(error);
    }
    for (const i of JSON.parse(body2).statuses) {
      console.log(`[${i.id}] ${i.text} by ${i.user.name}`);
    }
  }
  );
}
);
