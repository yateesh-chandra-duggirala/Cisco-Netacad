// Let us Create an array with strings
let days = ["Priya", "Raga", "Mallika"];

// Try to print the array
console.log(days)

// We can access the items with the help of index
console.log(days[1]);

// We can also modify the existing Value from the index.
days[2] = "Kusuma";
console.log(days);

// Print the length of the array with .length
console.log(days.length)

// So we get undefined if the index is not present in the existing array.
console.log(days[3]);

console.log(days[days.length - 2]);

// We can overwrite to the array
days[3] = "Cheli";
console.log(days);

// We can add the element as the last element of the Array.
days[days.length] = "Soumya";
console.log(days);