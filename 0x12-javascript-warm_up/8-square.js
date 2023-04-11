#!/usr/bin/node
const sizeee = Math.floor(Number(process.argv[2]));
if (isNaN(sizeee)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeee; i++) {
    let line = '';
    for (let j = 0; j < sizeee; j++) line += 'X';
    console.log(line);
  }
}
