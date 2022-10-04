#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const list2 = list.map(x => x * list.indexOf(x));
console.log(list2);
