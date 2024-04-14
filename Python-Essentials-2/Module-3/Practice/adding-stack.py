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
        return stack_list
    
class AddingStack(Stack) :
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def get_sum(self):
        return self.__sum

# Instantiating the object.
stack_object = AddingStack()

for i in range(0, 10, 2):
    stack_object.push(i)
print(stack_object.display())
print(stack_object.get_sum())