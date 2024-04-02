# Define a class named Stack
class Stack:
    # Create a constructor
    def __init__(self):
        # Add a new property to the Object
        self.__stack_list = []
        # When __ is added before the variable makes it private and can only be accessed inside the class
        # This is called Encapsulation.

# Instantiating the Object 
stack_object = Stack()

# Trying to access the __stack_list - (would raise an Attribute Error Exception)
print(len(stack_object.__stack_list))

# print(len(stack_object._Stack__stack_list)) # But this will print to the console.