// Arrays in JavaScript have a sort method available which, as you might guess, allows you to sort its elements. 
// This method takes as an argument a function that will compare two elements of the array. 
// The function should return zero if we consider the arguments to be the same, 
// a value less than zero if we consider the first one to be smaller than the second, 
// and a value larger than zero otherwise. 
// Take a look at the example:
let numbers = [50, 10, 40, 30, 20];
function compareNumbers(a, b) {
     let retVal = 0;
     if (a < b) {
         retVal = -1;
     } else if(a > b) {
         retVal = 1;
     }
     return retVal;
}
let sorted = numbers.sort(compareNumbers);
console.log(sorted);

// Task 1A. Try to modify the above piece of code to make it as short as possible. 
// Suggestions:
// - use an anonymous function;
// - use an arrow function;
// - consider skipping the if statement.

let numbers1 = [1, 60, 26, 21, 5]
let sortAsc = numbers1.sort((a, b) => a - b);
console.log("Ascending Order : ", sortAsc);

// Task 1B. Then modify the function so that the elements are sorted in descending order, 
// not in ascending order as in the example.
let sortDesc = numbers1.sort((a, b) => b - a);
console.log("Descending order : ",sortDesc);