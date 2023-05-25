#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
fs.readFile(fileName, function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
