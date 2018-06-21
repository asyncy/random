#!/usr/bin/env node

const { boolean, string, integer, list } = require('./lib/generate');

let args;
switch (process.argv[2]) {
  case 'boolean':
    console.log(boolean());
    break;
  case 'string':
    args = JSON.parse(process.argv[3]);
    console.log(string(args.length));
    break;
  case 'integer':
    args = JSON.parse(process.argv[3]);
    console.log(integer(args.low, args.high));
    break;
  case 'list':
    args = JSON.parse(process.argv[3]);
    console.log(list(args.type, args.length, args.string_length, args.integer_low, args.integer_high));
    break;
}
