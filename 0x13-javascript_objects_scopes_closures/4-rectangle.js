#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log('X'.repeat(this.width));
    for (let i = 0; i < this.height - 1; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let aux = 0;
    aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
