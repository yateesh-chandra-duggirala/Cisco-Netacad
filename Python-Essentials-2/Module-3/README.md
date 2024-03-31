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

# Stack : 
- A Stack is a structure developed to store data in a very specific way.
- The alternative name for the stack is LIFO (Last In First Out).
- A stack is an object with two elementary operations named push (Insertion into last) and pop (When an existing element is taken away from the top).
- Stacks are used very often in many classical algorithms and it is hard to imagine the implementation of many widely used tools without the use of stacks.
- Let us implement a stack in Python. This will be a very simple stack, and will show you how to do in two independent approaches : Procedural and objective.
- Let us start with the first one.

## a. The Procedural Approach
- First, you have to decide how to store the values which will arrive onto the stack.
- We suggest using the simplest of methods and employing a list for the job.
- Let us assume that the size of the stack is not limited in any way.
- Let us also assume that the last element of the list stores the top element.
- The stack itself is already created : 
    stack = []

- We are ready to define a function that puts a value onto the stack.
- Here are the presuppositions for it :
    a. The name for the function is push.
    b. The function gets one parameter (This is the value to be put onto the stack)
    c. The function returns nothing.
    d. The function appends the parameter's value to the end of the stack.
Now it is time for a function to take a value off the stack.
This is how you can do it.
    a. The name of the function is pop.
    b. The function does not get any parameters.
    c. The function returns the value taken from the stack.
    d. The function reads the value from the top of the stack and removes it.

## b. The Object-oriented Approach
- There are some weaknesses and also implementation can be improved in procedural approach, but in general the stack is fully implemented and you can use it if you need to.
- But more often you use it, the more disadvantages you will encounter :
a. The essential variable is highly vulnerable; anyone can modify it in an uncontrollable way, destroying the stack in effect; this does not mean that it has been done maliciously on the contrary, it may happen as a result of carelessness.
b. The functioning of the stack will be completely disorganized.
- It may also happen that one day you need more than one stack; You will have to create another list for the stack's storage and probably other push and pop functions too;
- It may also happen that you need not only push and pop functions, but also some other conveniences; You could certainly implement them but try to imagine what would happen if you had dozens of seperately implemented stacks.
- The object-oriented approach delivers solutions for each of these problems. They are :
a. Encapsulation : The ability to hide selected values against unauthorised access is called encapsulation; The encapsulated values can be neither accessed nor modified if you want to use them exclusively.
b. When you have a class implementing all the needed stack behaviors, you can produce as many stacks as you want; You need not copy or replicate any part of the code;
c. The ability to enrich the stack with new functions comes from inheritance; you can create a new class which inherits all the existing traits for the superclass, and adds some new ones.

- We are going to put the list into the class.
- We want the class to have one property as the stack's storage - we have to install a list inside each object of the class. (Note : Each Object has to have its own list - the list must not be shared among different stacks)
- Then We want the list to be hidden from the class user's sight.
- In contrast to other programming languages, Python has no means of allowing you to declare such property just like that.
- Instead, you need to add a specific statement or instruction.
- The properties have to added to the class manually.
- How do you guarantee that such an activity takes place every time the new stack is created?
- There is a simple way to do it - you have to equip the class with a specific function. - its specificity is dual :
    a. It has to be named in a strict way;
    b. It is invoked implicitly, when the new object is created
- Such a function is called a constructor, as its general purpose is to construct a new object.
- The constructor should I know everything about the object's structure and must perform all the needed initializations.
- Let us add a very simple constructor to the new class.

And now :
- The Constructor's name is always __init__.
- It has to have at least one parameter. The parameter is used to represent the newly created object - You can use the parameter to manipulate the object and to enrich it with the needed properties.
- The obligatory parameter is usually named self - It is only a convention, but you should follow it - It simplifies the process of reading and understanding your code.
- There is no trace of invoking the constructor inside the code. It has been invoked implicitly and automatically.
- Any change you make inside the constructor that modifies the state of the self parameter will be reflected in the newly created object.
- This means you can add any property to the object and the property will remain there until the object finishes its life or the property is explicitly removed.
- Now let us add just one property to the new object - a list for a stack. We will name it stack_list.

Note : 
- We have used dot notation, just like when invoking methods; This is the general convention for accessing an object's properties you need to name of the object, put a dot(.) after it and specify the desired property's name.. Do not use Parenthesis! you do not want to invoke a method, You just want to access the property.
- If you set a property's value for the very first time (like the constructor), you are creating it; from that moment on, the object has got the property and is ready to use its value.
- We have done something more in the code. We have tried to access the stack_list property from outside the class immediately after the creation of object and we want to check the current length of the stack.

We prefer stack_list to be hidden from the outside world. It is possible and simple but not very intuitive just by adding __(two underscores) before the list name.
- Because, When any class component has a name starting with two underscores(__), it becomes private that means that it can be accessed only from within the class.
- We can not see it from the outside world. This is how Python implements the encapsulation concept.

## Creating a Stack from Scratch.
- Now let us try to implement the two functions implementing the push and pop operations.
- Python assumes that a function of this kind should be immersed inside the class body just like a constructor.
- We want to invoke these functions to push and pop values. This means that they should both be accessible to every class's user (in contrast to the previously constructed list), which is hidden from the ordinary class's users. This is a public component.
- So you can not begin its name with two or more underscores.
- There is one more requirement : the name must have no more than one trailing underscores.
- As no trailing underscores at all fully meets the requirement, you can assume that the name is acceptable.
- Though the functions look familiar, but they have more parameters than their procedural counterparts.
- Here, Both the functions have a parameter named self at the first position of the parameters list.
- It is needed that all parameters should contain this parameter. It plays the same role as the first constructor parameter.
- It allows the method to access entities(properties and activities/Methods) carried out by the actual object.
- We can not omit it. Every time python invokes a method, it implicitly sends the current object as the first argument.
- This means the method is obligated to have atleast one parameter, which is used by the python itself. You do not have any influence on it.
- If the methods needs no parameter at all, this one 'self' must be specified anyway. It is designed to process just one parameter, you have to specify two and the first one's role is still the same.
- There is one more thing that requires explanation - the way in which methods are invoked from within the __stack_list variable.
- Fortunately, it is much simpler than it actually looks :
    a. the first stage delivers the object as a whole -> self
    b. Next, You need to get to the __stack_list list -> self.__stack_list.
    c. With __stack_list ready to be used, you can perform the third and last step -> self.__stack_list.append(val)
- The class declaration is complete and all the components have been listed. The class is ready to use now.
- Having such a class opens up some new possibilites.
- For example, You can now have more than one stack behaving in the same way.
- Each stack will have its own copy of private data, you will utilize the same set of methods. (as shown in stack-2-objects.py)
- There are two stacks created from same base class. They work independently.

### Add a new Class for handling stacks:
- The new class should be able to evaluate the sum of all elements currently stored in the stack.
- We do not want to modify the previously defined stack. it is already good enough in its applications and we don't want it to changed in any way. We want a new stack with new capabilities.
- In other words, we want to construct a subclass of the already existing Stack class.
- The first step is easy. Just define a new subclass pointing to the class which will be used as the superclass.

    ```
    class AddingStack(Stack) :
        pass
    ```
- The class does not define any new component yet, but that doesn't mean that it is empty. It gets all the components defined by its superclass - the name of the superclass is written before the colon directly after the new class name.
- This is what we want from the new stack :
    a. We want the push method not only to push the value onto the stack but also to add the value to the sum variable.
    b. We want the pop method not only to pop the value off the stack but also to subtract the value from the sum variable.

Firstly, Let us add a new variable to the class. It will be private variable.
- We do not want anybody to manipulate the sum variable.
- As you already know, adding a new property to the class is done by the constructor.
- You already know how to do that, but there is something really intriguing inside the constructor.
- The second line of the constructor's body creates a property named __sum - it will store the total of all the stack's values.
- But the line before it looks different. It is necessary.
- Contrary to many other languages, Python forces you to explicitly invoke a superclass's constructor. Omitting this point will have harmful effects - the object will be deprived of the __stack_list list. Such a stack will not function properly.
- This is the only time you can invoke any of the available constructors explicitly - it can be done inside the subclass's constructor.
- Note the Syntax : 
    a. You specify the superclass's name (this is the class whose constructor you want to run).
    b. You put a dot after it.
    c. You specify the name of the constructor.
    d. You have to point to the object (the class's instance) which has to be initialized by the constructor (That is why you have to specify the argument and use the self variable here)
    e. Note : Invoking any method (Including constructors) from outside the class never requires you to put the self argument's list - invoking a method from within the class demands explicit usage of the self argument, and it has to be put first on the list.
- Note : It is generally a recommended practice to invoke the superclass's constructor before any other initializations you want to perform inside the subclass. This is the rule we have followed in the snippet.

Secondly, Let us add two methods. but let us ask you : is it really adding ? We have these methods in the superclass already. Can we do something like that? Yes we can. 
- It means that we are going to change the functionality of the methods, not their names.
- We can say more precisely that the interface(The way in which the objects are handled) of the class remains the same when changing the implementation at the same time.
- Let us start with the implementation of the push function. This is what we explect from it :
    a. to add the value to the __sum variable.
    b. to push the value onto the stack.
- Note : The second activity has already been implemented inside the superclass - so we can use that. Furthermore, We have to use it, as there is no other way to access __stackList variable.

- Note the way we have invoked the previous implementation of the push method.
    a. We have to specify the superclass's name; This is neccessary in order to clearly indicate the class containing the method, to avoid confusing it with any other function of the same name;
    b. We have to specify the target object and to pass it as the first argument (It is not implicitly added to the invocation in this context).
- We see that the push method has been overridden - the same name as in the superclass now represents a different functionality.
- So far, we have defined the __sum variable, but we have not provided a method to get its value. It seems to be hidden. How can we reveal it and do it in a way that still protects it from modifications?
- We have to define a new method. We will name it get_sum. Its only task will be to return __sum value.