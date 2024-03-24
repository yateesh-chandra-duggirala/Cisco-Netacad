// Write three functions with the names add, sub, and mult, which will take two numerical arguments.
// The functions are to check if the given arguments are integers (use Number.isInteger). 
// If not, they return NaN, otherwise they return the result of addition, subtraction, or multiplication respectively.
//  The functions are to be declared using a function statement.
// Example of use and expected results:
// console.log(add(12, 10)); // -> 22
// console.log(mult(12, 10.1)); // -> NaN


function add(a, b) { 
    if (!Number.isInteger(a) || !Number.isInteger(b)) { 
        return NaN; 
    } 
    return a + b; 
}

function sub(a, b) { 
    if (!Number.isInteger(a) || !Number.isInteger(b)) { 
        return NaN; 
    } 
    return a - b; 
}

function mult(a, b) { 
    if (!Number.isInteger(a) || !Number.isInteger(b)) { 
        return NaN; 
    } 
    return a * b; 
}

console.log(add(12, 10));
console.log(mult(12, 10.1));