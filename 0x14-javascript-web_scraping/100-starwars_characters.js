#!/usr/bin/node

const r = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

r.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    JSON.parse(body).characters.forEach(character => {
      r.get(character, (err, res, body) => {
        if (err) console.log(err);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
