#!/usr/bin/node
exports.converter = function (base) {
  return (num) => {
    num = num.toString(base);
    return num;
  };
};
