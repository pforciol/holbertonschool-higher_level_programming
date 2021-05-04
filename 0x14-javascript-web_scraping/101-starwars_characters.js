#!/usr/bin/node

const r = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

r.get(url, async (err, res, body) => {
  if (err) console.log(err);
  else {
    for (const character of JSON.parse(body).characters) {
      const name = await new Promise((resolve, reject) => {
        r.get(character, (err, res, body) => {
          if (err) reject(err);
          else resolve(JSON.parse(body).name);
        });
      });
      console.log(name);
    }
  }
});
