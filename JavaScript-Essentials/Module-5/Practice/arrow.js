let add = function(a, b) {
    return a + b;
}
console.log(add(10, 20));

// this function can also be written as arrow function as mentioned below:

let add1 = (a, b) => {
    return a + b
}

console.log(add1(10, 30))

let add2 = (a, b) => a + b;
console.log(add2(89, 1))

let greetName = () => "Hello";
console.log(greetName())


let factorial = n => {
    return n > 1 ? n * factorial(n - 1) : 1;
}

console.log(factorial(3));