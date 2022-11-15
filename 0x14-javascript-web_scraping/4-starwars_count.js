#!/usr/local/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const movieData = JSON.parse(body).results;
    let count = 0;
    for (const index in movieData) {
      const movie = movieData[index];
      for (const cIndex in movie.characters) {
        const character = movie.characters[cIndex];
        if (character === 'https://swapi-api.hbtn.io/api/people/18/') count += 1;
      }
    }
    console.log(count);
  }
});
