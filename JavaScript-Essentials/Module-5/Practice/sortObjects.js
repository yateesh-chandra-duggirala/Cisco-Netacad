let numbers = [
    { 
        a : "Yateesh" , 
        b : 23, 
        c : 45
    },
    ,{
         a : "Chandra",
         b : 5,
         c : 22
    },
    {
        a : "Duggirala", 
        b : 11,
        c : 20
    }];

let sortAsc = numbers.sort((first, second) => first.a.localeCompare(second.a));
console.log("Ascending Order : ", sortAsc);
console.log(typeof(numbers[0].b))
