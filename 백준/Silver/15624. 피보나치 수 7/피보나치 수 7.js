const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const T = Number(input)

let [a, b] = [0, 1]

for (let i = 2; i <= input; i++){
    const tmp = (a+b) % 1000000007
    a = b
    b = tmp
}

console.log(b)