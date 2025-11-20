#!/usr/bin/node

const langs = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';

for (let i = 0; i < langs.length; i++) {
  if (i > 0) {
    output += '\n';
  }
  output += langs[i];
}

console.log(output);

