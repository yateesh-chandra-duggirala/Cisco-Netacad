try {
    let a = b;
} catch (error) {
    console.log("Caught " + error.message); // -> Caught ReferenceError: b is not defined
}
console.log("We handled the exception!"); // -> we handled the exception!
