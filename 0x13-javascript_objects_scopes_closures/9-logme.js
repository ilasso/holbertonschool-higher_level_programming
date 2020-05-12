#!/usr/bin/node
let Qlog = 0;
exports.logMe = function (arg) {
  console.log(`${Qlog}: ${arg}`);
  Qlog++;
};
