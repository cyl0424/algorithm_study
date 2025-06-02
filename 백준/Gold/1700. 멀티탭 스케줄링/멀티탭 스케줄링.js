const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K] = input[0].split(" ").map(Number);
const electrics = input[1].split(" ").map(Number);

let result = 0;
let plug = [];

for (let i = 0; i < K; i++){
    let current = electrics[i];
    if (plug.includes(current)) continue;

    if (plug.length < N){
        plug.push(current);
        continue;
    }

    let remove = -1;
    let maxIdx = -1;

    for (let j = 0; j < plug.length; j++){
        let nextUse = electrics.slice(i+1).indexOf(plug[j]);
        
        if (nextUse === -1){
            remove = j;
            break;
        }

        if (maxIdx < nextUse){
            maxIdx = nextUse;
            remove = j;
        }
    }

    plug[remove] = current;

    result++;
}

console.log(result);