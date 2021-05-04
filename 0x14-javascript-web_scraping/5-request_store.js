#!/usr/bin/node

const r = require('request');
const fs = require('fs');

r.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});
