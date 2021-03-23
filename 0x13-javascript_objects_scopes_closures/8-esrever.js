#!/usr/bin/node

exports.esrever = function (list) {
  const output = [];

  while (list.length) {
    output.push(list.pop());
  }

  return output;
};
