let state = "Andhrapradesh";

// 1. Character at a position can be known using charAt() function
let n = state.charAt(2);
console.log(n)

// 2. length of the string can be obtained by string.length
let len = state.length;
console.log(len)

// 3. slice method is used to obtain a substring
let sl_var = state.slice(6, 13)
console.log(sl_var.length)
console.log(typeof sl_var)

let spl = state.split("a");
console.log(spl)
console.log(typeof spl)
