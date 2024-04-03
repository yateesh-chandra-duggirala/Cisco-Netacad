/**Modify the calculator program that you made in Module 4 Section 2 in such a way that it will work in the loop until the user inputs Q in any of the prompt boxes. */

while(true) {
    let firstNumber = Number(prompt("Enter first number : "));
    let secondNumber = Number(prompt("Enter second number : "));
    let operand = prompt("Enter an operand : +, -, *, / :");
    let result;

    if(firstNumber === "Q" || secondNumber === "Q" || operand === "Q"){
        break;
    }
    
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
}