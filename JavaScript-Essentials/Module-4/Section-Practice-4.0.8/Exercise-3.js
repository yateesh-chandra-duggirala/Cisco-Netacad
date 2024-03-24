// Write a simple calculator application. 
// Ask the user for the following input, one by one: two numbers and a character representing a mathematical operation, one of "+", "-", "*", "/". 
// If the user input is valid, calculate the result and show it to the user. 
// If the user input is invalid, display a message that informs the user that an error has occurred.

// Remember that the value returned by the prompt function is of the type string. 
// You can use the Number.isNaN method to check if you get the correct number after conversion. 
// For example, calling Number.isNaN(10) will return false, while Number.isNaN(NaN) will return true.

let firstNumber = Number(prompt("Enter first number : "));
let secondNumber = Number(prompt("Enter second number : "));
let operand = prompt("Enter an operand : +, -, *, / :");
let result;

if(!Number.isNaN(firstNumber) && !Number.isNaN(secondNumber)){
    switch(operand){
        case "+" :
            result = firstNumber + secondNumber;
            break;
        case "-" :
            result = firstNumber - secondNumber;
            break;
        case "*" :
            result = firstNumber * secondNumber;
            break;
        case "/" :
            result = firstNumber / secondNumber;
        default:
            result = "Error - Unknown operand";
    }
} else {
    result = "An Unexpected Error occured";
}

alert(result)