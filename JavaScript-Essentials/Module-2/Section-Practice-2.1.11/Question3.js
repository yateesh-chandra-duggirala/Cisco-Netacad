// Question 3: Carry out a chain of conversions: create a Boolean from a BigInt 
// created from a Number that was created from a String. Start with the value "1234". Is it possible?

// Method 1 :
let string_value = "1234";
console.log(string_value);

// Convert the String to Number 
let num_value = Number(string_value);
console.log(num_value)

// Converting Number to BigInt
let big_int_value = BigInt(num_value);
console.log(big_int_value);

// Convert BigInt to Boolean
let boolean_value = Boolean(big_int_value);
console.log(boolean_value);

// Method 2 :
let bool_value = Boolean(BigInt(Number(String("1234"))));
console.log(bool_value);