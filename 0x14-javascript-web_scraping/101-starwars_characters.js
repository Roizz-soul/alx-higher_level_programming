#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const lst = {};
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const charac = JSON.parse(body).characters;
  for (let x = 0; charac[x]; x++) {
    request(charac[x], function (err, response, body) {
      if (err) {
        console.log(err);
      }
      const name = JSON.parse(body).name;
      lst[x] = name;
    });
  }
  function print () {
    for (let y = 0; lst[y]; y++) {
      console.log(lst[y]);
    }
  }
  setTimeout(print, 2000);
});
