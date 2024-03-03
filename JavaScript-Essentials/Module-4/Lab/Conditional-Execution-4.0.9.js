// Scenario
// During the last modification of the program with the contact list, we allow the user to add a new contact with the data entered by the user while the program is executing. 
// Let's go a step further – try to modify the program so that the user has a choice of what they want to do with the list. 
// They will have a choice of:
// - showing the first contact (first)
// - showing the last contact (last)
// - adding a new contact (new)
// When adding a new contact, check if the user has entered all the necessary data. 
// If at least one of the three values is missing (name, phone, or email) don't add the contact.

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

let choice = Number(prompt("Enter your choice : \n 1. Show the first Contact \n 2. Show the Last Contact \n 3. Add a new Contact", 0));
switch(choice) {
    case 1 : 
        alert(`The first contact : \nName : ${contacts[0].name} \n Phone : ${contacts[0].phone} \n Email : ${contacts[0].email}`);
        break;
    case 2 : 
        alert(`The last contact : \nName : ${contacts[contacts.length - 1].name} \n Phone : ${contacts[contacts.length - 1].phone} \n Email : ${contacts[contacts.length - 1].email}`);
        break;
    case 3 :
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
    default : 
        alert("Invalid Choice")
}