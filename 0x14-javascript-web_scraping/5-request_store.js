#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];
request(url, function (error, response, body) {
  if (!error) {
    fs.writeFile(filename, body, 'utf-8', err => {
      if (err) console.log(err);
    });
  }
});
