// Scenario
// We can improve our contact list program a bit by using loops. 
// You can now try to display not only the first or last contact, but all contacts in the list, regardless of their number.
// Additionally, try to enclose the whole program in a loop so that the user is repeatedly asked what they want to do. 
// The user can choose to:
// - display the first contact (first)
// - display the last contact (last)
// - display all contacts (all)
// - add a new contact (new)
// - exit the program (quit)
// After executing the selected action, the program will give the opportunity to choose again. 
// The program should end the actions only after the user gives a specified command, for example quit.

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

while(!quit){
    let choice = Number(prompt("Enter your choice : \n 1. Show the first Contact \n 2. Show the Last Contact \n 3. Display All contacts \n 4. Add a new Contact \n 5. Quit", 0));
    switch(choice) {
        case 1 : 
            alert(`The first contact : \nName : ${contacts[0].name} \n Phone : ${contacts[0].phone} \n Email : ${contacts[0].email}`);
            break;
        case 2 : 
            alert(`The last contact : \nName : ${contacts[contacts.length - 1].name} \n Phone : ${contacts[contacts.length - 1].phone} \n Email : ${contacts[contacts.length - 1].email}`);
            break;
        case 3 :
            for (let contact of contacts){
                // console.log(contact);
                console.log(`Name : ${contact.name} / Phone : ${contact.phone} / Email : ${contact.email}`);
                // alert(`Name : ${contact.name} / Phone : ${contact.phone} / Email : ${contact.email}`);
            }
            break;
        case 4 :
            let newContact = {}
            firstName = prompt("Enter the first name :");
            phone = Number(prompt("Enter Phone number : "));
            email = prompt("Enter the email : ");

            if(firstName && phone && email) {
                newContact.name = firstName;
                newContact.phone = phone;
                newContact.email = email;
                contacts[contacts.length] = newContact;
                console.log(newContact)
                alert("New contact added successfully")
                console.log(firstName, phone, email);
            } else {
                alert("Can not add the contact. All fields are mandatory")
                console.log(`Can not add the contact. All fields are mandatory`);
            }
            break;
        case 5 : 
            alert("You have quit Successfully.")
            quit = true;
            break;
        default : 
            alert("Invalid Choice")
    }
}