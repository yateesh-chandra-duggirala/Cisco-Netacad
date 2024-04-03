/**Write a program using a loop that will ask the user for the name of the movie (first prompt) 
 * and its rating from www.imdb.com (second prompt). 
 * The program will allow you to enter as many movies as you want into the movies array. 
 * Each element of the array will be an object, consisting of two fields: title and imdb. 
 * The input is completed if the user presses Cancel in the prompt dialog. 
 * Then the program should first print out to the console all movies that have a rating of less than 7, 
 * then those whose rating is greater than or equal to 7. 
 * Write the name of the movie and its rating next to each other, 
 * e.g.: Lost in Translation (7.7) */

let movie = []
while(true) {
    newObj = {}
    let movieName = prompt("Enter the Name of the movie : ");
    let rating = Number(prompt("Enter the Rating:"));
    if (movieName === null || rating === null) {
        break;
    } else {
        newObj.name = movieName;
        newObj.rating = rating;
        movie.push(newObj);
    }
}

console.log("Movies with ratings greater than 7 :")
for(let m of movie){
    if(m.rating > 7){
        console.log(`${m.name} -> ${m.rating}`);
    }        
}
