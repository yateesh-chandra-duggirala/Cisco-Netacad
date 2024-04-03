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

# OOP Properties :

1. Instance Variables :
- In general, Class can be equipped with two different kinds of data to form a class's properties. 
- The kind of class property exists when and only when it is explicitly created and added to an object.
- As you already know, this can be done during the object's initialization, performed by the constructor.
- Moreover, It can be done at any moment of the object's life. Furthermore, any existing property can be removed at any time.
- Such an approach has some important consequences :
    a. different objects of the same class may possess different sets of properties;
    b. there must be a way to safely chek if a specific object owns the property you want to utilize (Unless you want to provoke an exception - It is always worth considering).
    c. Each object carries its own set of properties - they do not interfere with one another in any way.
- Such variables are called instance variables.
- The word instance suggests that they are closely connected to the objects, not to the classes themselves.
- Let us take a closer look at Example-Class.

- Python objects, when created are gifted with a small set of predefined properties and methods. 
- Each Object has got them, whether you want them or not.
- One of them is a variable named __dict__ (It is a dictionary)
- The variable contains the names and values of all the properties the object is currently carrying. Let us make use of it safely to present an object's contents.
- Let us dive into the code now:
    a. the class named ExampleClass has a constructor, which unconditionally creates and instance variable named first. and sets it with the value passed through the first argument (from the class user's perspective). or the second argument (from the constructor's perspective); Note the default value of the parameter - any trick you can do with a regular function parameter can be applied to methods, too.
    b. The class also has a method which creates another instance variable named second.
    c. We have created three objects of the class ExampleClass, but all these instances differ :
        1. example_object_1 only has the property named first.
        2. example_obejct_2 has two properties : first and second
        3. example_object_3 has been enriched with a property named third just on the fly outside the class's code - this is possible and permissible.
    d. Modifying an instance variable of any object has no impact on all the remaining objects. Instance variables are perfectly isolated from each other.
- Let us run the same program but this time private variables
- When python sees that you want to add an instance variable to an object and you are going to do it inside any of the object's methods, It mangles the operation in the following way :
    a. It puts a class name before your name
    b. it puts an additional underscore at the beginning
- this is why __first becomes _ExampleClass_first
The name is now fully accessible from outside the class when you try to access variable name like 
`print(example_object._ExampleClass_first)`
- And we will get a valid result with no errors or exceptions.
- As you can see, making a property private is limited.
- The mangling will not work if you add a private instance variable outside the class code. In this case, it will behave like any other ordinary property.

2. Class Variables :
- A class variable is a property which exists in just one copy and is stored outside any object.
- Note : No instance variable exists if there is no object in the class; A class variable exists in one copy even if there are no objects in the class.
- Class variables are created differently to their instance siblings. The example will tell you more : ExampleClass-class.py
    a. There is an assignment in the first line of the class definition. - It sets the variable named counter to 0; Initializing the variable inside the class but outside any of its methods makes the variable a class variable.
    b. Accessing such a variable looks the same as accessing any instance attribute - you can see it in the constructor body; as you can see, the constructor increments the variable by one. In effect, The variable counts all the created objects.
- We must remember that :
    a. Class variables are not shown in an object's __dict__ (This is natural as class variables are not part of objects) but always we can try to look into the variable of the same name, but at the class level - We will show you this very soon.
    b. A class variable always presents the same value in all class instances (objects).
- Mangling a class variables' name has the same effects as those you are already familiar with.

3. Checking an attribute's existence :
- We may not expect that all objects of the same class have the same sets of properties
- Accessing a non-existing object attribute causes an AttributeError Exception.
- The try-except instruction gives you the chance to avoid issues with non-existent properties.
- Instead of doing so, We have a specific function that is provided by python to safely check if any object / class contains a specified property.
- the function is named hasattr and expect two arguments to be passed to it.
    a. The class or the object being checked.
    b. The name of the property whose existence has to be reported (Note : It has to be a string containing the attribute name, not the name alone).
- The function returns True or False.
- This is how you can utilize it.
- Do not forget the hasattr() function can operate on classes, too.
- you can use it to find out if a class variable is available, just like here in the example in the editor.
- The function returns True if the specified class contains a given attribute and False otherwise.

## Inner Life of Classes and Objects : 
- __dict__ (dictionary) method is used to find all the defined methods and attributes. Locate the context in which they exist : inside the object or inside the class.
- __name__ attribute is absent from the object - it exists only inside classes
- If you want to find the class of a particular object, you can use a function named type(), which is able to find a class which has been used to instantiate any object.
- __module__ is a string that stores the name of the module which contains the definition of the class.
- The module named "__main__" is actually not a module, but the file currently being run
- __bases__ is a tuple. The tuple contains classes (Not Class names) which are direct superclasses for the class.
- The order is the same as that used inside the class definition.
- We will show you only a very basic example, as we want to highlight how inheritance works.
- Also we will use this attribute when we discuss the object approach aspects of exceptions
- Note : Only classes have this attribute - objects do not.
- We have defined function named printbases(), designed to present the tuple's contents clearly.
- If the class has superclass, it prints the names of the super class
- A class without explicit superclasses points to an object (A predefined Python Class) as its direct ancestor.

## Reflection and Introspection : 
- Introspection is the ability of a program to examine the type or properties of an object at runtime.
- Reflection is the ability of a program to manipulate the vales, properties and/or functions of an object at runtime.
- In simple words, You do not have to know a complete class/ object definition to manipulate the object, as the object and/or its class contain the metadata allowing you to recognize its features during program execution.

## Investigating classes :
- Both Reflection and introspection enable a programmer to do anything with any object, no matter where it comes from.

## Inheritance in OOPS :
- When Python needs any class / object to be presented as a string (putting an object as an argument in the print() function invocation fits the condition) it tries to invoke the method named __str__() from the object and to use the string it returns.
- __str__() method is used to return the string (<__main__.Star object at 0x000001C80AD2A810>) something related to this by default.
- This behaviour can be changed by defining our own method of the name.
- The term inheritance is older than computer programming and it describes the common practice of passing different goods from one person to another upon that person's death.
- Inheritance is a common practice of passing attributes and methods from the superclass to a newly created class, called the subclass.
- Inheritance is a way of building a new class, not from scratch, but by using an already defined repertoire of traits.
- The new class inherits all the already existing equipment, but is able to add new ones if needed.
- The most important factor of the process is the relation between the superclass and all of its subclasses (Note : If B is a subclass of A and C is a subclass of B, this also means C is a subclass of A, as the relationship is fully transitive)
- A very simple example of two-level inheritance is presented here.
    ```
    class Vehicle :
        pass
    
    class LandVehicle(Vehicle) :
        pass
    
    class TrackedVehicle(LandVehicle) :
        pass
    ```
- From the above piece of code,
    1. The Vehicle class is the superclass for both LandVehicle and TrackedVehicle classes.
    2. The LandVehicle class is a subclass of vehicle and a superclass of TrackedVehicle at the same time.
    3. The TrackedVehicle class is a subclass of both the vehicle and LandVehicle classes.

## Python offers below functions of Inheritance :
### a. issubclass() :
- This is able to identify a relationship between two classes, and although its diagnosis is not complex, it can check if a particular class is a subclass of any other class.
- Returns True if ClassOne is a subclass of ClassTwo and False otherwise.
- Each class can be a subclass of itself.

### b. isinstance() :
- An object is an incarnation of a class.
- This means that the object is like a cake baked using a recipe which is included inside the class.
- To check if an object is a part of certain class or not, we use the function isinstance().
- The function returns True if the object is an instance of the class or False Otherwise.
- If a subclass contains atleast the same equipment as any of its superclasses, it means that objects of the subclass can do the same as objects derived from the superclass, It is an instance of the home class and any of its superclass.

### c. is operator :
- The is operator checks whether two variables (object_one and object_two here) refer to the same object.
- Do not forget that variables do not store the objects themselves, but only the handles pointing to the internal Python Memory.
- Assigning a value of an object to another variable does not copy the object, but only its handle. This is why an operator like is may be very useful in particular circumstances.

## How Python finds Properties and Methods:
- Let us look at the code in inheritance-example.py and analyze the code :
    a. There is a class named Super, which defined its own constructor used to assign the object's property, named name.
    b. The class defines the __str__() method too which makes the class able to present its identity in clear text form.
    c. The class is next used as a base to create a subclass named Sub. The Sub class defines its own constructor, which invokes the one from the superclass. Just by writing : Super.__init__(self, name)
    d. We have explicitly named the superclass and pointed to the method to invoke __init__(), providing all needed arguments.
    e. We have instantiated one object of class Sub and printed it.

Note : As there is no __str__() method within the Sub Class, the printed string is to be produced within the Super class. This means that the __str__() method has been inherited by the Sub Class.

- Also we can write super() instead of mentioning explicitly the class name
- super() function accesses the superclass without needing to know its name.
- super() function creates a context in which you do not have to pass the self argument to the method being invoked - this is why it is possible to activate the superclass constructor constructor using only one argument.
- Note : You can use this mechanism not only to invoke the superclass constructor, but also to get access to any of the resources available inside the superclass.
- For example, We can access the variables like class variables, instance variables
- When you try to access any object's entity, python will try to :
    a. First find it inside the object itself.
    b. find it in all classes involved in the object's inheritance line from bottom to top.
- if any of the above fails, an exception AttributeError is raised.
- As you know, all objects deriving from a particular class may have different sets of attributes and some of the attributes may be added to the object a long time after the object's creation.
- Multiple Inheritance occurs when a class has more than one superclass. 
- Syntactically, such inheritance is presented as a comma-separated list of superclasses put inside parentheses after the new classname - just like here.
- If more than one of the superclasses defines an entity of a particular name, It is overridden.
- the entity defined later in the inheritance sense overrides the same entity defined earlier.
- The feature can be intentionally used to modify default class behaviors when any of the classes needs to act in a different way to its ancestor.
- We can also say that Python looks for an entity from bottom to top, and is fully satisfied with the first entity of the desired name.
- When a class has two ancestors offering the same entity, and they lie on the same level, Python looks for the object components in the following order :
    a. Inside the object itself
    b. In its superclasses, from bottom to top
    c. If there is more than one class on a particular inheritance path, Python scans from left to right.

## Building Hierarchy of classes :
- If you divide a problem among classes and decide which of them should be located at the top and which should be placed at the bottom of the hierarchy, you have to carefully analyse the issue, but before we show how to do it, We want to highlight an interesting effect.
- It is nothing extraordinary, but remembering it may be a key to understanding how some codes work, and how the effect may be used to build a flexible set of classes.

    ```
    class One:
        def do_it(self):
            print("do_it from One")

        def doanything(self):
            self.do_it()


    class Two(One):
        def do_it(self):
            print("do_it from Two")


    one = One()
    two = Two()

    one.doanything()
    two.doanything()
        
    ```

- There are two classes named One and Two, while Two is derived from One. Nothing special. However one thing looks remarkable - the do_it() method.
- The do_it() method is defined twice : orginally inside One and subsequently inside Two. The essence of the example lies in the fact that it is invoked just one - inside One.
- The first invocation seems to be simple - invoking doanything() from the object named one will obviously activate the first of the methods.
- The second invocation needs some attention.
- It is simple, too if you keep in mind how Python finds class components.
- The second invocation will launch do_it() in the form existing inside the Two class, regardless of the fact that the invocation takes place within the One class.
- The situation in which the subclass is able to modify its superclass behavior is called polymorphism.
- The word means that one and the same class can take various forms depending on the redefinitions done by any of its subclasses.
- The method, redefined in any of the superclasses, thus changing the behavior of the superclass is called virtual.

- Inheritance is not the only way to construct adaptable classes. 
- You can achieve the same goals by using a technique named composition.
- Composition is the process of composing an object using other different objects.
- The objects used in the composition deliver a set of desired traits so we can say that they act like blocks used to build a more complicated structure.
- It can be said that :
    a. Inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, The complete recipe is contained inside the class itself and all its ancestors; The object takes all the class's belongings and makes use of them.
    b. Composition projects a class as a container able to store and use other objects where each of the objects implements a part of the desired class's behavior.
- Let us illustrate the difference by using the previously defined vehicles. The previous approach led us to a hierarchy of classes in which the top-most class was aware of the general rules used in turning the vehicle, but did not know how to control the appropriate components (wheels or tracks).
- The subclasses implemented this ability by introducing specialized mechanisms.
- Let us do the same thing, but using composition.
- the class like in the previous example, is aware of how to turn the vehicle, but the actual turn is done by a specialized object stored in a property named controller. The controller is able to control the vehicle by manipulating the relevant vehicles' parts.
- There are two classes named Tracks and Wheels – they know how to control the vehicle's direction. 
- There is also a class named Vehicle which can use any of the available controllers (the two already defined, or any others defined in the future) – the controller itself is passed to the class during initialization.
- A single inheritance class is always simpler, safer, and easier to understand and maintain
- Multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying these parts of the superclasses which will effectively influence the new class.
- Multiple inheritance may make overriding extremely tricky; moreover, using the super() function becomes ambiguous;

## Method Resolution Order (MRO) :
- If user tries to force (Top, Middle) in such a way that superclass precedes subclass, Then Python displays a message like :
    `TypeError : Can not create a consistent method resolution order (MRO) for bases Top, Middle.`
- Python's MRO cannot be bent or violated, not just because that is the way Python works, but also because it is a rule you have to obey.

## The Diamond Problem
- The second example of the spectrum of issues that can possibly arise from multiple inheritance is illustrated by a classic problem named the diamond problem.
- The name reflects the shape of the inheritance diagram
    a. There is the top most super class A
    b. There are two subclasses derived from A: B and C
    c. And there is also the bottom - most subclass named D, derived from B and C
- Some programming languages do not allow multiple inheritance at all and as a consequence, they won't let you build a diamond - this is the route that Java and C# have chosen to follow since their origins.
- Python however has chosen a different route - It allows multiple-inheritance and it does not mind if you write and run code with Multiple Inheritance, But Remember baout MRO - It is always in Charge

## Exception in OOPS :
- The object-oriented nature of Python's Exceptions makes them a very flexible tool, able to fit to specific needs, even those you do not yet know about.
- Before we dive into the objective face of exceptions, we want to show you some syntactical and semantic aspects of how python treats the try-except block, as it offers a little more than what we have presented so far.
- The first feature we want to discuss here is an additional, possible branch that can be placed inside the try-except block - It is the part of the code strating with else. as shown in exception-oop.py
- A code labelled in this way is executed when no exception has been raised inside the try : part. 
- We can say that exactly one branch can be executed after try : - either the one beginning with except (do not forget there can be more than one branch of this kind) or the one starting with else.
- Note : The else branch has to be located after the last except branch.
- There is another part headed by the finally keyword, which is the last branch of the code designed to handle exceptions.
- These two variants : else and finally are not dependent in any way, and they can coexist or occur independently
- The finally block is always executed, no matter what happened earlier, even when raising an exception, no matter whether this has been handled or not.

### Exception are classes :
- Exceptions are classes, Furthermore when an exception is raised, an object of the class is instantiated and goes through all levels of program execution, looking for the except branch that is prepared to deal with it.
- Such an object carries some useful information which can help you to precisely identify all aspects of the pending situation.
- To achieve that goal, Python offers a special variant of the exception clause.
- As we can see, the except statement is extended, and contains an additional phrase starting with the as keyword, followed by an identifier.
- The identifier is designed to catch the exception object so you can analyze its nature and draw some useful conclusions.
- The identifier's scope covers its except branch, and does not go any further.
- The example presents a very simple way of utilizing the received object - just print it out and it contains a brief message describing the reason.
- The same message will be printed if there is no fitting except block in the code and python is forced to handle it alone.
- All are built-in Python Exceptions form a hierarchy of classes. There is no obstacle to extending it if you find it reasonable.
- As a tree is a perfect example of a recursive data structure, a recursion seems to be the best tool to traverse through it. The print_exception_tree() function takes two arguments.

### Detailed Anatomy of exceptions : 
- Let us take a closer look at the exception's object, as there are some really interesting elements here (We will return to the issue soon when we consider Python's input / Output base techniques, as their exception subsystem extends these objects a bit).
- The BaseException class introduces a property named args.
- It is a tuple designed to gather all arguments passed to the class constructor.
- It is empty if the construct has been invoked without any arguments, or contains just one element when the constructor gets one argument.

- We have used the function to print the contents of the args property in three different cases, where the exception of the Exception class is raised in three different ways.
- To make it more spectacular, we have also printed the object itself, along with the result of the __str__() invocation.
- the first case looks routine - there is just the name Exception after the raise keyword. This means that the object of this class has been created in a most routine way.
- The second and third cases may look a bit weird at first glance, but there is nothing odd here - these are just the constructor invocations. In the second raise statement, the constructor is invoked with one argument and in the third with two.

### Creating Own Exception :
- The exceptions hierarchy is neither closed nor finished, and you can always extend it if you want or need to create your own world populated with your own exceptions.
- It may be useful when you create a complex module which detects errors and raises exceptions, and you want the exceptions to be easily distinguishable from any others brought by Python.
- This can be done by defining your own, new exceptions as subclasses derived from predefined ones.
- If you want to create an exception which will be utilised as a specialised case of any built-in exception, derive it from just this one.
- If you want to build your own hierarchy, and do not want it to be closely connected to Python's exception tree, derive it from any of the top exception classes, like exception.
- Imagine that you have created a brand new arithmetic, ruled by your own laws and theorems.
- It is clear that division has been redefined, too, and has to behave in a different way than routine dividing.
- It is also clear that this new division should raise its own exception, different from the built-in ZeroDivisionError, But it is reasonable to assume that in some circumstances, you may want to treat all Zero Divisions in the same way.
- Look into MyZeroDivisionError.py . We have the following observations : 
    a. We have defined our own exception, named MyZeroDivisionError, derived from the built-in ZeroDivisionError.
    b. As you can see, we have decided not to add any new components to the class
    c. In effect, An exception of this class can be depending on the desired point of view - treated like a plain ZeroDivisionError, or considered seperately.
    d. The do_the_division() function raises either a MyZeroDivisionError or ZeroDivisionError Exception, depending on the argument's value
- The function is invoked four times in total, while the first two invocations are handled using only one except branch and the last two ones with two different branches, able to distinguish the exceptions (The order of the branches make fundamental difference).
- When you are going to build a completely new universe filled with completely new creatures that having nothing in common with all the familiar things, you may want to build your own exception structure.
- For example, If you work on a large simulation system which is intended to model the activities of a pizza restaurant, it can be desirable to form a seperate hierarchy of exceptions.
- You can start building it by defining a general exception as a new base class for any other specialized exception, It can be done as:

    ```
    class PizzaError(Exception):
        def __init__(self, pizza, message):
            Exception.__init__(self, message)
            self.pizza = pizza
    ```
- Note : We are going to collect more specific info here than a regular Exception does, so our constructor will take two arguments :
    a. One specifying a pizza as a subject of the process
    b. And one containing a more or less precise description of the problem.
- As we can see, we pass the second parameter to the superclass constructor, and save the first inside our own property.
- A more specific problem can require a more specific exception.
- it is possible to derive the new class from the already defined PizzaError class :
    ```
    class TooMuchCheeseError(PizzaError):
        def __init__(self, pizza, cheese, message):
            PizzaError.__init__(self, pizza, message)
            self.cheese = cheese
    ```
- The TooMuchCheeseError Exception needs more information than the regular PizzaError exception, so we add it to the constructor - the name cheese is then stored for further processing.
- one of these is raised inside the make_pizza() function when any of these two erroneous situations is discovered : a wrong pizza request, or a request for too much cheese.
- Note : 
    a. removing the branch starting with except TooMuchCheeseError will cause all appearing exception to be classified as PizzaError
    g. removing the branch starting with except PizzaError will cause the TooMuchCheeseError exceptions to remain unhandled, and will cause the program to terminate.