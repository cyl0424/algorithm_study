const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(" ").map(Number);
let maze = [];

for (let i = 1; i <= N; i++){
    maze.push(input[i].split("").map(Number));
}

let queue = [[0, 0]];

let dx = [1, -1, 0, 0];
let dy = [0, 0, 1, -1];

let visited = Array.from({ length: N }, () => Array(M).fill(false));
visited[0][0] = true;

let head = 0;

while (head < queue.length){
    let [y, x] = queue[head];

    head ++;

    for (let i = 0; i < 4; i++){
        let nx = x + dx[i];
        let ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= M || ny >= N || maze[ny][nx] !== 1) continue;
        if (!visited[ny][nx]){
            visited[ny][nx] = true;
            maze[ny][nx] = maze[y][x] + 1 // 거리 업데이트
            queue.push([ny, nx]);
        }
    }

}

console.log(visited[N-1][M-1] ? maze[N-1][M-1] : -1);