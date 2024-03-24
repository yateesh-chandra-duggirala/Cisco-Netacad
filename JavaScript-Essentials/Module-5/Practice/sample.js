// function showMessage(message) {
//     console.log(`Message: ${message}`);
// }

// let sm = showMessage;
// sm("Hi Priya")
// console.log(typeof sm)

function add(a, b) {
    return a + b;
}
function multiply(a, b) {
    return a * b;
}

console.log(add(3, 5))

function operation(func, first, second) {
    return func(first, second);
}
console.log(operation(add, 10, 20));
console.log(operation(multiply, 10, 20));