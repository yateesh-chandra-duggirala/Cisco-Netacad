let number = prompt("Enter any number : ")

switch (true) {
    case number > 0 && number % 2 == 0:
        console.log("Even Number");
        alert("Even Number");
        break;
    case number > 0 && number % 2 != 0 :
        console.log("Odd number");
        alert("Odd Number");
        break;
    case number < 0 :
        console.log("Negative number");
        alert("Negative Number");
        break;
    default :
        console.log("Not a Number");
        alert("Invalid Input");    
}