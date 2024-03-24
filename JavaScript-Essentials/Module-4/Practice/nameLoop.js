let names = [];
let isOver = false;
while (!isOver) {
    let name = prompt("Enter another name or press cancel.");
    if (!name) {
        isOver = true;
    } else {
        names.push(name);
    }
}
 
for (let i = 0; i < names.length; i++){
    console.log(names[i]);
}