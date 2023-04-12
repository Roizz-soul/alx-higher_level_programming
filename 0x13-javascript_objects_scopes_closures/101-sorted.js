#!/usr/bin/node
const dict = require('./101-data.js').dict;
const Dict = {};
for (const key in dict) {
  if (Dict[dict[key]] === undefined) {
    Dict[dict[key]] = [key];
  } else {
    Dict[dict[key]].push(key);
  }
}
console.log(Dict);
