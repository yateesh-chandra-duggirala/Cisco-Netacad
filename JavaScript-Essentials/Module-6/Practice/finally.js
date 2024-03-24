// let a = 10;
// try {
//     a = 5;
// } finally {
//     console.log(a);
// }
// console.log(a);

let a = 10;
try {
    a = b;  // ReferenceError
} finally {
    console.log("Finally"); // -> 10
}
console.log(a);
