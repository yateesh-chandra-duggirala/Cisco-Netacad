// Write a function that will calculate the n-th element of the Fibonacci sequence. 
// This sequence is defined by a formula:
// So each element of the sequence (except the first two) is the sum of the previous two. 
// For example: F1 = 1, F2 = F1 + F0 = 1, F3 = F2 + F1 = 2 and F6 = F5 + F4 = 8. 
// The function should use recursion. 
// In the definition, use a function expression (store an anonymous function in a variable).

// Example of use and expected results:
// console.log(fibbRec(4)); // -> 3
// console.log(fibbRec(7)); // -> 13

let fibbRec = function(ele) {
    let value = 0;

    if (ele != 0 ){
    
        if (ele === 1){
            value = 1;
        } else {
            value =  fibbRec(ele - 1) + fibbRec(ele - 2);
        }
    }
    return value;
}

console.log(fibbRec(4));
console.log(fibbRec(7));