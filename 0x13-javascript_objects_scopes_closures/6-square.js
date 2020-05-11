#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    if (char == null) {
      char = 'X';
    }
    console.log(char.repeat(this.width));
    for (let i = 0; i < this.height - 1; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
