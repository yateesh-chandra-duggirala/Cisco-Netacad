// Rewrite the functions from the previous task (Exercise - 2) using an arrow function expression, 
// trying to write them in the shortest possible form.

// Example of use and expected results:
// console.log(sub(12, 10)); // -> 2
// console.log(mult(10, 10.1)); // -> NaN

let add = (a , b) => (Number.isInteger(a) && Number.isInteger(b)) ? a + b : NaN
let sub = (a , b) => (Number.isInteger(a) && Number.isInteger(b)) ? a - b : NaN
let mult = (a , b) => (Number.isInteger(a) && Number.isInteger(b)) ? a * b : NaN

console.log(sub(12, 10));
console.log(mult(10, 10.1));