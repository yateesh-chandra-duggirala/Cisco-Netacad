// Write a program that will print out (to the console) consecutive integers 10 times, 
// in two-second intervals (start with the number 1). 
// Use the functions setInterval, clearInterval and setTimeout.

// Expected results:
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10

let i = 1;
let consoleValue = () => {
    console.log(i++)
}

let consoleFunction = (callback) => {
    let timerId = setInterval(callback, 2000);
    setTimeout(function(){
        clearInterval(timerId);
    }, 21000);
}

consoleFunction(consoleValue);