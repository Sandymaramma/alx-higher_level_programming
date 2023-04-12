#!/usr/bin/node
// script that prints message depending on number of arguments passed

const argsCount = process.argv;

// if...else statements were used to check number of arguments passed
// console.log()function was used to print all messages

if (argsCount.length === 0) {
  console.log('No argument');
} else if (argsCount.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
