// Variables are declared using two keywords in two ways:
// 1. Using "let" keyword.
// 2. Using "var" keyword.

var height;
console.log(height);    //undefined
console.log(weight);    //Uncaught ReferenceError: weight is not defined

//let prevents us from defining another variable with same name.

var height;
var height;

// var allows the re declaration of the variable

/*Always use let to declare any variable in Javascript...*/