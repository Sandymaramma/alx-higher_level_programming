#!/usr/bin/node
// script that computes and prints a factorial

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);

const result = factorial(arg);
console.log(result);
