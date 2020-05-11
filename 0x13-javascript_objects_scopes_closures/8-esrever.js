#!/usr/bin/node

exports.esrever = function (list) {
  let j = 0;
  for (let i = list.length - 1; i !== 0 && i > j; i--) {
    let aux = list[j];
    list[j] = list[i];
    list[i] = aux;
    aux = 0;
    j++;
  }
  return list;
};
