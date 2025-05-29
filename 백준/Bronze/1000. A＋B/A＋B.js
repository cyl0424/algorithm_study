const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

let [a, b] = [Number(input[0]), Number(input[1])]

console.log(a+b)