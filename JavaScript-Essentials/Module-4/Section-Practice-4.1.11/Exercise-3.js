// There are ten different numbers in the following numbers array:
// let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
// Write a program that first writes out all these numbers on the console, then only those that are even 
// (hint: the remainder of dividing an even number by 2 is equal to 0),
// then only those that are larger than 10 and at the same time smaller than 60.

let numbers = [21, 45, 100, 12, 11, 78, 61, 4, 39, 22];
let numbers_even = [];
let numbers_cond = [];

for (let num of numbers) {
    if(num % 2 == 0){
        numbers_even.push(num);
    }
    if(num > 10 && num < 60){
        numbers_cond.push(num)
    }
}

console.log(numbers);
console.log(numbers_even);
console.log(numbers_cond)