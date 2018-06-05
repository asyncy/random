#!/usr/bin/env node

const { boolean, string, integer, list } = require('./lib/generate');

switch (process.argv[2]) {
  case 'boolean':
    console.log(boolean());
    break;
  case 'string':
    console.log(string(process.argv[3]));
    break;
  case 'integer':
    console.log(integer(process.argv[3], process.argv[4]));
    break;
  case 'list':
    console.log(list(process.argv[3], process.argv[4], process.argv[5], process.argv[6], process.argv[7]));
    break;
}
