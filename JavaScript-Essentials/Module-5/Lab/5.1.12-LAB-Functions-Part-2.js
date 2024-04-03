/**
 * We will use the functions to add one more item of functionality. 
 * Arrays have a sort method that allows us to sort their elements. 
 * To this method, we pass a function which should compare two elements of the array and decide which one is smaller and which one is bigger. 
 * If the first element is smaller, the function returns a value less than zero, if they are equal it returns zero, and if the first is larger, it returns a value greater than zero. 
 * For example, the array:
 * let numbers = [10, 50, 40, 20];
 * can be sorted in ascending order with a call:

    numbers.sort(function (a, b) {
        let retVal = 0;
        if (a > b) {
        retVal = 1;
        } else {
        retVal = -1;
        }
        return retVal;
    });

 * or more simply:
    numbers.sort((a, b) => a - b);

 * Give the user the option to select a sort action from the list.
 * When this option is selected, the user should be able to specify whether they want to sort the contacts by name, phone, or email.
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

let quit = false;

let showContact = function(contacts, i) {
    if (contacts instanceof Array && contacts[i]) {
        console.log(`${contacts[i].name} / ${contacts[i].phone} / ${contacts[i].email}`);
    }
}

let showAllContacts = function(contacts) {
    if (contacts instanceof Array) {
        for (let contact of contacts) {
            console.log(`${contact.name} / ${contact.phone} / ${contact.email}`);
        }
    }
}

let addNewContact = function(contacts, name, phone, email) {
    if (contacts instanceof Array && name && phone && email) {
        contacts.push({
            name: name,
            phone: phone,
            email: email
        });
    }
}

let sortFunction= (contactList) => {
    let sortChoice = Number(prompt("Enter the element you want to sort : \n 1. Email \n 2. Name \n 3. Phone \n 4. Exit", 0));
    switch(sortChoice){
        case 1 :
            let sortEmail = contactList.sort((first, second) => first.email.localeCompare(second.email));
            // console.log(sortEmail);
            sortEmail.forEach((contact, index) => {
                console.log(`Contact ${index + 1}: \n \t Name: ${contact.name} \t Phone: ${contact.phone} \t Email: ${contact.email} \n`);
            });
            break;
        case 2 :
            let sortName = contactList.sort((first, second) => first.name.localeCompare(second.name));
            sortName.forEach((contact, index) => {
                console.log(`Contact ${index + 1}: \n \t Name: ${contact.name} \t Phone: ${contact.phone} \t Email: ${contact.email} \n`);
            });
            break;
        case 3 :
            let sortPhone = contactList.sort((first, second) => first.phone.localeCompare(second.phone));
            sortPhone.forEach((contact, index) => {
                console.log(`Contact ${index + 1}: \n \t Name: ${contact.name} \t Phone: ${contact.phone} \t Email: ${contact.email} \n`);
            });
            break;
        default:
            alert("Invalid Choice");
    }
}

while(!quit){
    let choice = Number(prompt("Enter your choice : \n 1. Show the first Contact \n 2. Show the Last Contact \n 3. Display All contacts \n 4. Add a new Contact \n 5. Sort the element \n 6. Quit", 0));
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
            phone = prompt("Enter Phone number : ");
            email = prompt("Enter the email : ");
            addNewContact(contacts, firstName, phone, email);
            break;
        case 5 :
            sortFunction(contacts);
            break;
        case 6 : 
            alert("You have quit Successfully.");
            quit = true;
            break;
        default : 
            alert("Invalid Choice");
    }
}