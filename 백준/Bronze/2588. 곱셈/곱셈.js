const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let a = Number(input[0]);
let b = input[1].split('');

let one = a * Number(b[2]);
let two = a * Number(b[1]);
let three = a * Number(b[0]);

console.log(one);
console.log(two);
console.log(three);
console.log((three*100) + (two * 10) + one);