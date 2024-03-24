// Modify the previous program so that it asks the user for the first and last number it uses instead of 100 and 0 
// (hint: use the prompt dialog).
// Check if the entered values are correct (that the initial value is greater than the final value).
let input1 = Number(prompt("Enter the first value :"));
let input2 = Number(prompt("Enter the last value :"));
if(!Number.isNaN(input1) && !Number.isNaN(input2) && (input1 < input2)){
    for(let i = input1; i < input2; i++) {
        console.log(i);
    }    
} else {
    console.log("Unable to complete the request");
}
