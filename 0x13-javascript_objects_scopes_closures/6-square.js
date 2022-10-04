#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
