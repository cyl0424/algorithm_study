const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [a, b] = input[0].split(' ').map(Number);

console.log(a*b)