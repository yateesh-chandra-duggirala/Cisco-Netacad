// define an array :
list = ["H", "E", "A", "R", "T"];

console.log(list[0]);   // prints the H
console.log(typeof list[0]);    // prints string.

// instance of Operator. Instance of means type.
// India is instance of Earth, But not vice versa.
// Result would be in boolean.

let variable = "h"
console.log("H" instanceof Array);  // String cannot be instance of array.
console.log(list instanceof Array); // Array is an instance of array.

// indexOf() method from Array
console.log(list.indexOf("R")); // If the Item is found in the array, It prints the index
console.log(list.indexOf("B")); // If the item is not found, Then -1 will be printed.

// push() method is used to insert an element into the Array at the end.
list.push("Y");
console.log(list);

// Unshift() method is used to insert an element at the beginning.
list.unshift("P");
list.unshift("A", "O");
console.log(list);

// pop() method helps us to remove the last element from the array.
list.pop()
console.log(list)

// shift() method helps us to remove element from the beginning
list.shift()
console.log(list)

// reverse() method helps us to print the reverse of the array
console.log(list.reverse())

// slice() method helps us to  slice a part from the array.
console.log(list.slice(3))
console.log(list.slice(1, 4))


// concat() adds the items from both the lists.
let names = ["Olivia", "Emma", "Mateo", "Samuel"];
let otherNames = ["William", "Jane"];
let allNames = names.concat( otherNames);
console.log(allNames)