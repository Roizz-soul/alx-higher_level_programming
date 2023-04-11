#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let b = 0;
  while (b < num) {
    console.log('C is fun');
    b++;
  }
}
