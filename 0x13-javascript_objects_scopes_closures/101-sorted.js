#!/usr/bin/node

const dict = require('./101-data').dict;
const output = {};

for (const entry in dict) {
  if (!output[dict[entry]]) output[dict[entry]] = [];
  output[dict[entry]].push(entry);
}

console.log(output);
