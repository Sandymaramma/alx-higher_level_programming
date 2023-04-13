const list = require('./100-data').list;

const multipliedList = list.map((value, index) => {
  return value * index;
});

console.log(`Original list: ${list}`);
console.log(`Multiplied list: ${multipliedList}`);
