#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg, 10);
let output = '';

if (isNaN(x)) {
  output = 'Missing number of occurrences';
} else {
  for (let i = 0; i < x; i++) {
    if (i > 0) {
      output += '\n';
    }
    output += 'C is fun';
  }
}

console.log(output);

