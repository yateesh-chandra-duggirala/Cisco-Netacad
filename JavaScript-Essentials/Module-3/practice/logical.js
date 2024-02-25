const a = false;
const b = true;
const c = false;
const d = true;
console.log(a && b && c || d);      // true.
console.log(a && b && (c || d));    // false.

let nr = 0;
let year = 1970;
let names = "Alice";
let empty = "";
console.log(!nr);       // true
console.log(!year);     // false
console.log(!names);    // false
console.log(!empty);    // true
console.log(!!nr);      // false
console.log(!!names);   // true

// Exercise 3
// If answer is false, first operator is evaluated/ True, Second operator
console.log(true && 1991); 
console.log(false && 1991);
console.log(2 && 5);      
console.log(0 && 5);       
console.log("Alice" && "Bob");
console.log("" && "Bob");   
 
// OR operator prints first operator if true or else second operator
console.log(true || 1991);  
console.log(false || 1991); 
console.log(2 || 5); 
console.log(0 || 5); 
console.log("Alice" || "Bob"); 
console.log("" || "Bob");
console.log(0 || 0); 
