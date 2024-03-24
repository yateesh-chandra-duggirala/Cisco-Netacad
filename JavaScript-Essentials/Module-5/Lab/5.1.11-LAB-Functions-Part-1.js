/**
 * Scenario
 * Our program has grown quite a bit, making it a little hard to read. 
 * It is especially visible in the switch instruction, where most of the logic is enclosed. 
 * Try to organize your program code by using functions. Define and call three functions in the appropriate places:
    a. showContact: the function should take two arguments; the first is the list of contacts, and the second is the index number of the contact to display; inside the function, check if the correct arguments are passed, that is, if the contacts are an array (use the instanceofArray construction for this);
    b. showAllContacts: the function should take one argument, the list of contacts; inside the function, check if the given argument is an array;
    c. addNewContact: the function should take four arguments, a contact list and the data of the new contact, that is: name, phone, and number; before adding a new contact, check if the passed argument is an array and if the new contact data have any value.
 */

let contacts = [{
    name: "Maxwell Wright",
    phone: "(0191) 719 6495",
    email: "Curabitur.egestas.nunc@nonummyac.co.uk"
}, {
    name: "Raja Villarreal",
    phone: "0866 398 2895",
    email: "posuere.vulputate@sed.com"
}, {
    name: "Helen Richards",
    phone: "0800 1111",
    email: "libero@convallis.edu"
}];

quit = false;

// Create functions
let showContact = (contactList, index) => {
    if(contactList instanceof Array && contactList[index]){
        alert(`The first contact : \nName : ${contactList[index].name} \n Phone : ${contacts[index].phone} \n Email : ${contacts[index].email}`);
    }
}

let showAllContacts = (contactList) => {
    if(contactList instanceof Array){
        for (let contact of contactList){
            console.log(`Name : ${contact.name} / Phone : ${contact.phone} / Email : ${contact.email}`);
        }
    }
}

let addNewContact = (contactList, firstName, phone, email) => {
    if (contactList instanceof Array && firstName && phone && email) {
        contacts.push({
            name: firstName,
            phone: phone,
            email: email
        });
    }
}

while(!quit){
    let choice = Number(prompt("Enter your choice : \n 1. Show the first Contact \n 2. Show the Last Contact \n 3. Display All contacts \n 4. Add a new Contact \n 5. Quit", 0));
    switch(choice) {
        case 1 : 
            showContact(contacts, 0);
            break;
        case 2 : 
            showContact(contacts, contacts.length - 1);
            break;
        case 3 :
            showAllContacts(contacts);
            break;
        case 4 :
            firstName = prompt("Enter the first name :");
            phone = Number(prompt("Enter Phone number : "));
            email = prompt("Enter the email : ");
            addNewContact(contacts, firstName, phone, email);
            break;
        case 5 : 
            alert("You have quit Successfully.");
            quit = true;
            break;
        default : 
            alert("Invalid Choice");
    }
}