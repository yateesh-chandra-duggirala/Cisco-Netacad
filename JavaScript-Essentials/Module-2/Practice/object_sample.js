let name1 = "Calvin";
let surname1 = "Hart";
let age1 = 66;
let email1 = "CalvinMHart@teleworm.us";

let name2 = "Mateus";
let surname2 = "Pinto";
let age2 = 21;
let email2 = "MateusPinto@dayrep.com";

// Most Convenient Way is to create object 

let empObj1 = {
    name : "Calvin",
    surname : "Hart",
    age : 66,
    email : "CalvinHart@teleworm.us"
}

let empObj2 = {
    name : "Mateus",
    surname : "Pinto",
    age : 21,
    email : "MateusPinto@dayrep.com"
}

console.log(empObj1.name);
console.log(empObj2.name);

empObj1.age = 50;
console.log(empObj1.age);

console.log(empObj1);

console.log(empObj1.phone)

// We can add a new property to the object
empObj2.phone = 7984020480
console.log(empObj2)

// Also we can delete an existing property from the object
delete empObj2.prop

console.log(empObj2);