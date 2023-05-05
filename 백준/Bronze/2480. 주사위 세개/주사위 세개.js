const fs = require('fs');

const numbers = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);

const a = numbers[0];
const b = numbers[1];
const c = numbers[2];

if (a == b && b == c) {
    console.log(10000 + a * 1000);
} else if (a == b & b != c) {
    console.log(1000 + a * 100);
} else if (a == c & c != b) {
    console.log(1000 + a * 100);
} else if (b == c & b != a) {
    console.log(1000 + b * 100);
} else {
    let max_num = Math.max(a, b, c);
    console.log(max_num * 100);
}