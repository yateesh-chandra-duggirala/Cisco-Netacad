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

# Instantiating two different objects.
stack_object_1 = Stack()
stack_object_2 = Stack()

# Push some elements into the list.
stack_object_1.push(2)
stack_object_2.push(4)
stack_object_1.push(6)

# Now display the stack to view
stack_object_1.display()

# Now Pop an item from the stack.
stack_object_2.push(stack_object_1.pop())

# Display the items from the stacks again.
stack_object_1.display()
stack_object_2.display()
