#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
  process.exit(1);
}
let max = 0;
let secmax = 0;
for (let i = 2; i < process.argv.length; i++) {
  if (parseInt(process.argv[i], 10) > max) {
    secmax = max;
    max = parseInt(process.argv[i], 10);
  } else if (parseInt(process.argv[i], 10) >= secmax) {
    secmax = parseInt(process.argv[i], 10);
  }
}
console.log(secmax);
