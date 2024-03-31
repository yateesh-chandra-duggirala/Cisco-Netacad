# Defining the Stack Class
class Stack:
    # Defining the constructor function.
    def __init__(self):
        # Add just one property to the new object.
        self.stack_list = []

# Instantiating the Object
stack_object = Stack()
print(len(stack_object.stack_list))