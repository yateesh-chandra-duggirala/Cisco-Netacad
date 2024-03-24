// console.log("start"); // -> start
// throw "Priya"; // -> Uncaught 100
// console.log("end");

console.log("start"); // -> start
try {
    throw 100;
} catch (error) {
    console.log(error); // -> 100
}
console.log("end"); // -> end
