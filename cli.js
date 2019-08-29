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
    console.log(JSON.stringify(list(args.type, args.length, args.stringLength, args.integerLow, args.integerHigh)));
    break;
}6
