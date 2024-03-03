/**
 * The contents of the object describing the position of the vessel named "Mareno" are written on the console:
    LATITUDE -> 40.07288 
    LONGITUDE -> 154.48535 
    COURSE -> 285.6 
    SPEED -> 14.0 
    IMO -> 9175717 
    NAME -> MARENO
The code presented below is used for this. 
Complete the program by declaring the missing object in place of the three dots:
 */

let vessel = {
    LATITUDE : 40.07288,
    LONGITUDE : 154.48535,
    COURSE : 285.6,
    SPEED : 14.0,
    IMO : 9175717,
    NAME : "MARENO"
}
 
for( let key in vessel) { 
    console.log(`${key} -> ${vessel[key]}`); 
}