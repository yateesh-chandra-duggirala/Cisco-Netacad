// Question 1: Write a code that will create variables and initialize them with values of Boolean, Number, BigInt, String, and undefined types using (when possible) literals and constructor functions

let num_var = 1
let num_var_const = Number(30)
let string_var = "Hello"
let string_var_const = String("Hi")
let big_var = 123n
let big_var_const = BigInt(3n)
let bool_var = false
let bool_var_const = Boolean(true)
let undef_var = undefined

// Question 2 : Print all values and all types of those values using console.log. Try to use string interpolation to display the value and type at the same time with a single console.log call, e.g. in the following form: 1000 [number].
console.log(`${num_var} : [${typeof num_var}]`)
console.log(`${num_var_const} : [${typeof num_var_const}]`)
console.log(`${string_var} : [${typeof string_var}]`)
console.log(`${string_var_const} : [${typeof string_var_const}]`)
console.log(`${big_var} : [${typeof big_var}]`)
console.log(`${big_var_const} : [${typeof big_var_const}]`)
console.log(`${bool_var} : [${typeof bool_var}]`)
console.log(`${bool_var_const} : [${typeof bool_var_const}]`)
console.log(`${undef_var} : [${typeof undef_var}]`)