#!/usr/bin/node
// script that prints first argument passed to it

const [arg] = process.argv.slice(2);

// if...else statement was used to check if arg exis
if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
