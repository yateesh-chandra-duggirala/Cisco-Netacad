# Define a class Stack
class Stack:
    
    # Create a constructor with a private variable __stack_list
    def __init__(self):
        self.__stack_list = []
    
    # Create a method to push an item to the stack
    def push(self, val):
        self.__stack_list.append(val)
    
    # Create a method to pop an item from the stack
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
    # Define a method that displays the stack.
    def display(self):
        stack_list = self.__stack_list
        print(stack_list)
    

# Instantiating the object.
stack_object = Stack()

# Push some elements into the list.
stack_object.push(2)
stack_object.push(4)
stack_object.push(6)

# Now display the stack to view
stack_object.display()

# Now Pop an item from the stack.
print(stack_object.pop())

# Display the items from the stacks again.
stack_object.display()
