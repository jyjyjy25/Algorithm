const fs = require('fs');

const inputs = fs.readFileSync('/dev/stdin').toString().split('\n');
const T = +inputs[0];
for(let i=0; i<T; i++) {
    const str = inputs[i+1];
    let answer = str[0] + str[str.length - 1];
    console.log(answer);
}