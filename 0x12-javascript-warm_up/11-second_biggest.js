#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
  process.exit(1);
}
let max = 0;
let secmax = 0;
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i] > max) {
    secmax = max;
    max = process.argv[i];
  } else if (process.argv[i] > secmax) {
    secmax = process.argv[i];
  }
}
console.log(secmax);
