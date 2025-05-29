const input = require('fs').readFileSync('/dev/stdin').toString().trim();


const alphabets = "abcdefghijklmnopqrstuvwxyz".split('');
let result = [];

alphabets.forEach(element => {
    result.push(input.indexOf(element));
});

console.log(...result);