/**Exercise 1: 
 * Write your own div function that will take two call arguments and 
 * return the result of dividing the first argument by the second. 
 * In JavaScript, the result of dividing by zero is the value Infinity 
 * (or -Infinity, if we try to divide a negative number). Change this. 
 * If you pass 0 as the second argument, your function should throw a RangeError exception with the appropriate message.
 * Prepare a test call of the function for both valid division and division by zero.*/

let div = (a, b) => {
    
    if (b === 0) {
        throw new RangeError("Can't divide by Zero");
    }
    return a / b;
}

let firstNumber = Number(prompt("Enter the first number : "));
let secondNumber = Number(prompt("Enter the second number : "));

console.log(div(firstNumber, secondNumber));