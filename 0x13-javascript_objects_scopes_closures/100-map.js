#!/usr/bin/node

// Import the `list` array from the `100-data.js` file
const { list } = require('./100-data');

// Log the original `list` array
console.log('Original list:', list);

// Create a new array by multiplying each element of the original array by its index
const multipliedList = list.map((number, index) => number * index);

// Log the new array
console.log('Multiplied list:', multipliedList);
