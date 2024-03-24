// Question 3: We are setting up our small library of books about JavaScript programming. 
// We have three books and want to prepare a list of them. 
// We will store three pieces information about each book: title, author, and number of pages:

// Speaking JavaScript, Axel Rauschmayer, 460;
// Programming JavaScript Applications, Eric Elliott, 254;
// Understanding ECMAScript 6, Nicholas C. Zakas, 352.

// Create an array of three objects representing the books. 
// Each object must have the following properties: title, author, pages.

library = 
[{
    title : "Speaking JavaScript",
    author : "Axel Rauschmayer",
    pages : 460
},
{
    title : "Programming JavaScript Applications",
    author : "Eric Elliott",
    pages : 254
},
{
    title : "Understanding ECMAScript 6",
    author : "Nicholas C. Zakas",
    pages : 352
}]

console.log(library)


// Question 4: Add a new book to the collection: 
// Learning JavaScript Design Patterns, by Addy Osmani, 254 pages. 
// Use the appropriate method to do this, which will attach the book at the end of the array. 
// Display the length of the array and, in turn, all the book names in the collection.

new_book = {
    title : "Learning JavaScript Design Patterns",
    author : "by Addy Osmani",
    pages : 254
}

library.push(new_book);
console.log(`The length of the Books in the library = ${library.length}`);
console.log(`The names of the Books in the library : ${library[0]["title"]}, ${library[1]["title"]}, ${library[2]["title"]}, ${library[3]["title"]}`)


// Question 5: Use the slice command to copy the last two books to the new array.
let sliceBooks = library.slice(-2);
console.log(sliceBooks);


// Question 6: The first book from the collection is lost in unexplained circumstances. 
// You have already accepted the loss, so remove it from the array. 
// Which method will you use for this purpose? 
// Display the length of the array and all the names of the books from the collection in turn.
library.shift()   // Shift method removes the beginning element from the array.
console.log(library.length);
console.log(`The names of the Books in the library : ${library[0]["title"]}, ${library[1]["title"]}, ${library[2]["title"]}`);


// Question 7: Display the sum of the pages of all the books from the collection.
console.log(`Sum Of Pages : ${library[0].pages + library[1].pages + library[2].pages}`);