#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const fileName = process.argv[2];
const data = process.argv[3];
fs.writeFile(fileName, data, 'utf8', function (err) {
  if (err) {
    return console.error(err);
  }
});
