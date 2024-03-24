// Rewrite the function from Task 5 using an arrow function expression, but try to shorten its code as much as possible 
// (use conditional operators, and try not to use additional variables other than the parameter n).

let fibbRec = element =>  element == 0 ? 0 : (element == 1 ? 1 : fibbRec(element - 1) + fibbRec(element - 2));

console.log(fibbRec(4));
console.log(fibbRec(7));