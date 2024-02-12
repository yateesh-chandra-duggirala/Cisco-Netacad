console.log(Number(42));    // 42
   
console.log(Number("11"));  // 11
console.log(Number("0x11")); // 17
console.log(Number("0o11"));    // 9
console.log(Number("0b11"));    // 3
console.log(Number("12e3"));    // 12000
console.log(Number("Infinity"));    // infinity
console.log(Number("text")); //NaN
   
console.log(Number(14n)); //14
console.log(Number(123456789123456789123n)); // 123456789123456789123

   
console.log(Number(true)); // 1
console.log(Number(false)); // 0
   
console.log(Number(undefined)); // NaN
   
console.log(Number(null));  // 0

console.log("\n\n\n\n\n");

console.log(Boolean(true)); // true
   
console.log(Boolean(42)); // true
console.log(Boolean(0)); // false
console.log(Boolean(NaN)); // False
   
console.log(Boolean("text"));   // true
console.log(Boolean(""));   // false
   
console.log(Boolean(undefined)); // false
   
console.log(Boolean(null));    // false



console.log("\n\n\n\n")

console.log(BigInt(11)); // 11n
console.log(BigInt(0x11)); // 17n
console.log(BigInt(11e2)); // 1100n
   
console.log(BigInt(true)); // 1n
   
console.log(BigInt("11")); //11n
console.log(BigInt("0x11")); // 17n
   
// console.log(BigInt(null)); // NaN
   
// console.log(BigInt(undefined)); // undefined
   
// console.log(BigInt(NaN));  //NaN    