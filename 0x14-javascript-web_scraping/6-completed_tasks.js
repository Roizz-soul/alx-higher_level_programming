#!/usr/bin/node

const process = require('process');
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let num = 0;
  let uid = 1;
  let i = 0;
  const lst = JSON.parse(body);
  for (i = 0; lst[i]; i++) {
    if ((lst[i].completed === true) && (lst[i].userId === uid)) {
      num++;
    }
    if ((lst[i + 1] !== undefined) && (lst[i].userId !== lst[i + 1].userId)) {
      uid = lst[i + 1].userId;
      if (lst[i].userId !== 1) {
        console.log('  \'' + lst[i].userId + '\': ' + num + ',');
      } else {
        console.log('{ \'' + lst[i].userId + '\': ' + num + ',');
      }
      num = 0;
    }
  }
  console.log('  \'' + lst[i - 1].userId + '\': ' + num + ' }');
});
