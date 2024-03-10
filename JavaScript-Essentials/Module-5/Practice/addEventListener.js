i = 0
function clickMe() {
    console.log("Click No : ", i);
    i++;

    if( i == 10){
        window.removeEventListener("click", clickMe);
        console.log("Click limit reached");
    }
}

window.addEventListener("click", clickMe);