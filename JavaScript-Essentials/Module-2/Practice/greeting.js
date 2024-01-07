// variable should be declared, before it is used.
// Variable is an entity that is able to vary (Change).
// Constant is an entity that never changes.
// There are some naming conventions that should be followed when we are about to declare any variable.
// 1. Variable name should not be a keyword/ reserved word. (if, while, else, for)
// 2. Variables may contain : Lower case, upper case, digits, underscore, dollar
// 3. They should start only with lower or upper case or underscore
// 4. Variables support declaring either camelCase, snake_case
// 5. Variables should not contain spaces.
// 6. Make sure that the variable name is clearly declared.
// 7. Let us take three variables : test, Test and TEST (These three are different Variables).
// 8. Variable is case sensitive.

// height of rectangle ->  heightOfRectangle (Camel Case)
// height_of_rectangle (Snake Case)

let greetings = "Hello.!";
let counter = 100;
console.log(greetings);
greetings= 1;
console.log(greetings);

greetings = "Hello.!";
greetings = greetings + counter;
console.log(greetings);