#!/usr/bin/node

if (process.argv.length > 3) {
  const array = process.argv.slice(2).map(Number);

  array.splice(array.indexOf(Math.max.apply(null, array)), 1);
  console.log(Math.max.apply(null, array));
} else {
  console.log(0);
}
