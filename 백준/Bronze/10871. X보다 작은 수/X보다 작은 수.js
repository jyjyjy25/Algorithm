const fs = require('fs');

const inputs = fs.readFileSync('/dev/stdin').toString().split('\n');

const first_line = inputs[0].split(" ").map(Number);
const N = first_line[0];
const X = first_line[1];
const arr_num = inputs[1].split(" ").map(Number);

for(let i=0; i<N; i++) {
    if (arr_num[i] < X) {
        console.log(arr_num[i] );
    }
}
