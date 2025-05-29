const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [N, target] = input[0].split(' ').map(Number);
let numbers = input[1].split(' ').map(Number);

let result = numbers.filter(number => number < target);

console.log(...result);