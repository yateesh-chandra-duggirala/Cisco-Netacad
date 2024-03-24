let number = prompt("Enter a number", 0);
 
if(number > 0){
    console.log("positive");
    alert("positive");
} else if (number < 0) {
    console.log("Negative");
    alert("Negative");
} else if (number == 0) {
    console.log("Zero");
    alert("Zero");
} else {
    console.log("NaN");
    alert("Not an integer")
}