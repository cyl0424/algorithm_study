const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const matrix = [];

for (let i = 1; i <= N; i++){
    matrix.push(input[i].split("").map(Number));
}

const areaSize = [];
const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

for (let i = 0; i < N; i++){
    for (let j = 0; j < N; j++){
        if (matrix[i][j] !== 1) continue;
        
        let stack = [[i, j]];
        let size = 0;
        
        while (stack.length > 0){
            const [cx, cy] = stack.pop();
            
            if (cx < 0 || cy < 0 || cx >= N || cy >= N) continue;
            if (matrix[cx][cy] !== 1) continue;
            
            matrix[cx][cy] = -1;
            size ++;
            
            for (let dir = 0; dir < 4; dir++){
                stack.push([cx + dx[dir], cy + dy[dir]]);
            }
        }
        
        areaSize.push(size);
    }
}

console.log(areaSize.length);
areaSize.sort((a, b) => a - b);
areaSize.forEach(element => console.log(element));