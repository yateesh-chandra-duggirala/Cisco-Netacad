// let us do the same function from exercise 5 but without Callback.

let counter = 1;
let intervalId = setInterval(function () {
    console.log(counter++);
}, 2000);
setTimeout(function () {
    clearInterval(intervalId)
}, 21000);