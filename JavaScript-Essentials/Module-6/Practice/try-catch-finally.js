// let a = 10;
// try {
//     a = b;  
// } catch (error) {
//     console.log("An Error!");
// } finally {
//     console.log("Finally!");
// }
// console.log(a);

let a = 10;
try {
    a = b;  // First ReferenceError
} catch (error) {
    console.log(b); // Second ReferenceError
 
} finally {
    console.log("Finally!");
}
