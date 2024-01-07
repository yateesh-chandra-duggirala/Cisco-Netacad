var globalGreeting = "Good"

function testFunction(){
    var localGreeting = "Morning";
    console.log("Function : ")
    console.log(globalGreeting);
    console.log(localGreeting);
}

testFunction();

console.log("main program:");
console.log(globalGreeting);
console.log(localGreeting); // will not be executed since its scope is only local.