#!/usr/bin/node
let sMax = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  sMax = args[args.length - 2];
}
console.log(sMax);
