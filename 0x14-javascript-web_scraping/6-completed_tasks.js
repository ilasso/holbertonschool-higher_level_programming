#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsontask = JSON.parse(body);
  const tskdonebyuser = {};
  for (let i = 0; i < jsontask.length; i++) {
    // console.log(jsontask[i])
    if (jsontask[i].completed === true) {
      if (tskdonebyuser[jsontask[i].userId] === undefined) {
        tskdonebyuser[jsontask[i].userId] = 1;
      } else {
        tskdonebyuser[jsontask[i].userId]++;
      }
    }
  }
  console.log(tskdonebyuser);
});
