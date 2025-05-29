const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let numbers = input[1].split(' ').map(Number);

console.log(Math.min(...numbers), Math.max(...numbers));