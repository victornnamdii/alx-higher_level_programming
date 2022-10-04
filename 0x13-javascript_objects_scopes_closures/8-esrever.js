#!/usr/bin/node
exports.esrever = function (list) {
  const rArray = [];
  for (let i = 0; list[i]; i++) {
    rArray.unshift(list[i]);
  }
  return rArray;
};
