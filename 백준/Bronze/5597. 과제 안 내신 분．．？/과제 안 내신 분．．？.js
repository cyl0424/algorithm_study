const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

let result = [];

for (let i = 1; i < 31; i++){
    if (!input.includes(i)){
        result.push(i);
    }
}

console.log(...result);