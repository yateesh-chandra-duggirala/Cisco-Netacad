// Question 1: Create an object that describes a train ticket and store it in the ticket variable. The object must have three fields:

// starting station (key name "from", give the name of the nearest station in your area as a value);
// end station (key name to, give any other station within 100km as a value);
// the price of the ticket (key name price, give the amount you would like to pay for this ticket as a value).
// The object must be created using curly brackets, in which all created fields will be listed immediately. Then display the values of all fields of the ticket on the console.


let train_ticket = {
    from : "Anakapalle",
    to : "Eluru",
    price : 90
}

console.log(`Train Ticket from : ${train_ticket.from}`);
console.log(`Train Ticket To : ${train_ticket.to}`);
console.log(`Train Ticket Price : ${train_ticket.price}`);