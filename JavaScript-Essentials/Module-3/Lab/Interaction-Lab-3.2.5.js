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
    
    let last = contacts.length - 1;
    
    contacts[0].name = window.prompt("Enter the Name of first Person");
    contacts[0].phone = window.prompt("Enter the Phone of first Person");
    contacts[0].email = window.prompt("Enter the email of first Person");

    contacts[last].name = window.prompt("Enter the Name of the last Person");
    contacts[last].phone = window.prompt("Enter the Phone of the last Person");
    contacts[last].email = window.prompt("Enter the email of the last Person");
    
    alert(`${contacts[0].name} / ${contacts[0].phone} / ${contacts[0].email}\n${contacts[last].name} / ${contacts[last].phone} / ${contacts[last].email}`);
    console.log(`${contacts[0].name} / ${contacts[0].phone} / ${contacts[0].email}`);
    console.log(`${contacts[last].name} / ${contacts[last].phone} / ${contacts[last].email}`);
