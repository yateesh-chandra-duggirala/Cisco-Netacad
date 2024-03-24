// Write an iterative version of the function from Exercise 5 (use the for loop). 
// Declare the function using a function statement.

function fibonacci(n){
    let a = 0, b = 1;
    for(i = 2; i<=n; i++){
        let c = a;
        a = b;
        b +=c ;
    }
    return b;
}

console.log(fibonacci(4))
console.log(fibonacci(7))