# Procedural vs Object Oriented Programming :

## Procedural Approach :
- In the procedural approach, It is possible to distinguish two different and completely separate worlds :
    a. World of Data (Populated with variables of different kinds)
    b. World of Code (Inhabited by code grouped into modules and functions)
- Functions are able to use Data, but not vice versa. Furthermore, Functions are able to use the data in an unauthorized way. (When a sine function gets the bank account balance as a parameter).
- Data can not use functions, but sometimes, It can with the help of methods.
- Methods are functions that are invoked from with in the data, not beside them.

## Object Approach :
- This approach suggests a completely different way of thinking.
- The data and the code are enclosed together in the same world, divided into classes.
- Every class is like a recipe which can be used when you want to create a useful object. you may produce as many objects as you need to solve your problem.
- Each object has a set of traits (They are called properties or attributes) and is able to perform a set of activities (called methods).
- The recipes may be modified if they are inadequate for a specific purpose and in effect, new classes may be created.
- These new classes inherit properties and methods from the originals and usually add some new ones, creating new, more specific tools.

- Objects are incarnations of ideas expressed in classes, like a cheesecake on your plate is an incarnation of the idea expressed in a recipe printed in an old cookbook.
- The objects interact with each other, exchanging data or activating their methods.
- A properly construncted class and able to protect the sensible data and hide it from the unauthorized modifications.
- There is no clear border between data and code as they live as one in objects.
- All these concepts are not as abstract as you may at first suspect.
- On the contrary, they all are taken from real-life experiences and therefore are extremely useful in computer programming : They reflect real facts, relationships and circumstances.

# Class Hierarchies :
- Class is just like a Category as a result of precisely defined similarities.

### Example 1 : Vehicles
![https://skillsforall.com/content/pe2/1.0/m3/course/en-US/assets/ef63ccc83d2c691f736d63825fe422a931678405.png](vehicle.png)

- From this, Vehicles class is very broad. We have to define some more specialized classes, Then the Specialized classes are the subclasses.
- For all of them, The Superclass will be Vehicle Class.
- The hierarchy always grows from top to bottom like tree roots and not branches.
- The most general, and the widest, class is always at the top (the super class) while its descendants are located below (The Subclasses).
- There are many possible classifications. We have chosen subclasses based on the environment and say that there are four subclasses.
    a. Land Vehicles
    b. Water Vehicles
    c. Air Vehicles
    d. Space Vehicles
- Consider the first subclass : Land Vehicles may be again divided depending on the method with which they impact the ground. We can enumerate :
    a. Wheeled Vehicles
    b. Tracked Vehicles
    c. Hovercrafts
- The Hierarchies we have created is illustrated by the Direction basically.
- Note the direction always should point to the super class. And the top level is an exception as it does not have its super class

### Example 2 : Animals
![https://skillsforall.com/content/pe2/1.0/m3/course/en-US/assets/c0de1a4c1e5247cec5b9306561bc713a6a8b725f.png](animal.png)
- We can say that all animals can be divided into four subclasses :
    a. mammals
    b. reptiles
    c. birds
    d. fish
    e. amphibians
- Again we have subclasses for mammals :
    i. Wild Mammals
    ii. domesticated mammals.

# What is an Object :
- A class is a set of objects. An Object is a being belonging to a class.
- An Object is an incarnation of the requirements, traits, qualities assigned to a specific class.
- Classes form a hierarchy.
- This means that an object belonging to a specific class belongs to all the superclasses at the same time. It may also means that any object belonging to a super class may not belonging to any of its subclasses.
- Any Personal car is an object belonging to the wheeled vehicles class.
- It also means that the same car belongs to all superclasses of its home classes; Therefore it is a member of the vehicles class too.
- Each subclass is more specialized than its superclass. Conversely, each superclass is more general (more abstract) than any of its subclasses.

# Inheritance :
- Let us define one of the fundamental concepts of object programming, named inheritance.
- Any Object bound to a specific level of a class hierarchy inherits all the traits (as well as the requirements and qualities) defined inside any of the superclasses.
![https://skillsforall.com/content/pe2/1.0/m3/course/en-US/assets/4d95e44e08db5ac873bc510dd1731d3888cd0d40.png](inheritance.py)
- The object's home class may define new traits (as well as requirements and qualities) which will be inherited by any of its subclasses.

## What does an object have ?
- The object programming convention assumes that every existing object may be equipped with 3 groups of attributes.
  a. an object has a name that uniquely identifies it within its home namespace (although there may be some anonymous objects, too).
  b. an object has a set of individual properties which  makes it original, unique or outstanding (Although it is possible that some objects may have no properties at all.)
  c. an object has a set of abilities to perform specific activities, able to change the object itself or some of the other objects.

- There is a small hint which can helpt us identify any of the three spheres above. :
    a. Noun -> Name of the object
    b. Adjective -> Property of the object
    c. Verb -> Activity of the object

- Two sample phrases should serve as a good example
    A pink Cadillac went Quickly
    Object Name : Cadillac
    Home Class : Wheeled Vehicles
    Property : Color (Pink)
    Activity : Go (Quickly)

# The First Class :
- Object programming is the art of defining and expanding classes.
- A class is a model of a very specific part of reality, reflecting properties and activities found in the real world.
- the class defined at the beginning are too general and imprecise to cover the largest possible number of real cases.
- There is no obstacle to defining new or more precise subclasses.
- They will inherit everything from their superclass, so the work that went into its creation is not wasted.
- The new class may add new properties and new activities and therefore may be more useful in specific applications.
- Obviously, It may be used as a super class for any number of newly created subclasses.
- the process does not need to have an end. You can create as many classes as you need.
- The class you define has nothing to do with the object. (The existence of class does not mean that any of the compatible objects will be automatically created.)
- The class itself is not able to create an object - You have to create yourself and python allows us to do so.

- The definition of class begins with the keyword class.
- The keyword is followed by an identifier which will name the class.
- It should have a colon at the end as classes like functions form their own nested block.
- The content inside the block defines all the class's properties and activities.

# The First Object :
- The newly created class becomes a tool that is able to create new objects.
- the tool has to be used explicitly, on demand
- To create an object, You need to assign a variable to store the newly created object of the class and create an object at the same time.
- The class name tries to pretend that it is a function.
- The newly created object is equipped with everything the class brings; as this class is completely empty, the object is empty, too
- The act of creating an object of the selected class is also called Instantiation (as the object becomes an instance of the class).
