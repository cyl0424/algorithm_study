const input = require('fs').readFileSync('/dev/stdin').toString().trim().split("");

let sticks = [];
let result = 0;

for (let i = 0; i < input.length; i++){
    let current = input[i];

    if (current == '(' && input[i+1] == ')'){
        result += sticks.length;
        i++;
    }else if(current == '('){
        sticks.push(current);
    }else{
        sticks.pop();
        result++;
    }
}
console.log(result);