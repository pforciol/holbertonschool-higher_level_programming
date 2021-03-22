#!/usr/bin/node

function factorial (num) {
  if (num > 0) {
    return num * factorial(num - 1);
  }
  return 1;
}

console.log(factorial(Number(process.argv[2])));
