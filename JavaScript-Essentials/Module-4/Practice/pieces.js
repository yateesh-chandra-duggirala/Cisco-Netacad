let unitPrice = 10
let total
let pieces = prompt("How many pieces do you want?", 0);
if (pieces > 0) {
    total = unitPrice * pieces;
    console.log("Mee bill : ", total);
    alert("Mee bill : " + total);
}
console.log(total);