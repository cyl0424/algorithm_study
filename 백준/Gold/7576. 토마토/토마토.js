const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [M, N] = input[0].split(' ').map(Number);
const box = input
  .slice(1)
  .map(line => line.split(' ').map(Number));

const queue = [];
const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];


for (let y = 0; y < N; y++) {
  for (let x = 0; x < M; x++) {
    if (box[y][x] === 1) {
      queue.push([y, x]);
    }
  }
}

let head = 0;
while (head < queue.length) {
  const [y, x] = queue[head++];
  for (let dir = 0; dir < 4; dir++) {
    const ny = y + dy[dir], nx = x + dx[dir];
    if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue;
    if (box[ny][nx] !== 0) continue; 
    box[ny][nx] = box[y][x] + 1;
    queue.push([ny, nx]);
  }
}

let days = 0;
for (let y = 0; y < N; y++) {
  for (let x = 0; x < M; x++) {
    if (box[y][x] === 0) { 
      console.log(-1);
      process.exit();
    }
    days = Math.max(days, box[y][x]);
  }
}

console.log(days - 1);