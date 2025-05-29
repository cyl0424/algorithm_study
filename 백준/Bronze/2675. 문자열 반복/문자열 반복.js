const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = parseInt(input[0], 10);
const result = [];

for (let i = 1; i <= T; i++) {
  const [R, S] = input[i].split(' ');
  const repeatCount = parseInt(R, 10);
  let P = '';

  for (const char of S) {
    P += char.repeat(repeatCount);
  }

  result.push(P);
}

console.log(result.join('\n'));