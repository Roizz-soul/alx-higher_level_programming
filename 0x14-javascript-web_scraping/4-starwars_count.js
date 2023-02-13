#!/usr/bin/node

const process = require('process');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const lst = JSON.parse(body).results;
  let j = 0;
  for (let x = 0; lst[x]; x++) {
    for (let i = 0; lst[x].characters[i]; i++) {
      if (lst[x].characters[i] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        j++;
      }
    }
  }
  console.log(j);
});
