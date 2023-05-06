const fs = require('fs');

const inputs = fs.readFileSync('/dev/stdin').toString().split('\n');

const first_line = inputs[0].split(" ").map(Number);
const N = first_line[0];
const M = first_line[1];

let arr1 = [];
for (let i=0; i<N; i++) {
    arr1.push(inputs[1+i].split(" ").map(Number));
}

let arr2 = [];
for (let i=N; i<2*N; i++) {
    arr2.push(inputs[1+i].split(" ").map(Number));
}

let answer = [];
for(let i=0; i<N; i++) {
    let temp = [];
    for(let j=0; j<M; j++) {
        temp.push(arr1[i][j] + arr2[i][j]);
    }
    answer.push(temp);
}

let output;
for(let i=0; i<N; i++) {
    output = '';
    for(let j=0; j<M; j++) {
        output += answer[i][j].toString() + " ";
    }
    console.log(output);
}