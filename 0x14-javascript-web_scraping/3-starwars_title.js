#!/usr/bin/node

const process = require('process');
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  console.log(err || JSON.parse(body).title);
});
