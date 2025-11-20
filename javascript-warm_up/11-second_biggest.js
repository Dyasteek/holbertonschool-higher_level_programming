#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const nums = args.map(arg => parseInt(arg, 10));
  nums.sort((a, b) => b - a);
  const unique = [...new Set(nums)];
  
  if (unique.length < 2) {
    console.log(0);
  } else {
    console.log(unique[1]);
  }
}
