#!/usr/bin/node
// script that prints message depending on number of arguments passed

const argsCount = process.argv.length - 2;

// if...else statements were used to check number of arguments passed
// console.log()function was used to print all messages

if (argsCount === 0) {
	console.log('No argument');
} else if (argsCount === 1) {
	console.log('Argument found');
} else {
	console.log('Argument found');
}
