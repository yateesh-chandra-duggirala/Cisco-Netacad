function largest(a, b, c) {
    if (a > b && a > c) {
     return a;
    } else if (b > a && b > c) {
     return b;
    } else {
     return c;
    }
}

// console.log(largest(4, 1, 9));
// console.log(largest(1, 1, 2));
console.log(largest(2, 2, 1));