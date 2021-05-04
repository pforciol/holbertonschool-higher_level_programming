#!/usr/bin/node

const r = require('request');

r.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    let count = 0;
    const movies = JSON.parse(body).results;
    movies.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.includes('people/18/')) count++;
      });
    });
    console.log(count);
  }
});
