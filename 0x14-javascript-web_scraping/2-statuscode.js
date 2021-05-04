#!/usr/bin/node

const r = require('request');

r.get(process.argv[2], (err, res) => {
  if (err) console.log(err);
  else console.log('code: ' + res.statusCode);
});
