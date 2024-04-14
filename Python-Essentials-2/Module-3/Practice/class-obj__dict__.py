# Let us try to understand the difference betweeen the __dict__ variables of object and class.
# Define the class ExampleClass.
class ExampleClass :
    # The class defines one class variable named varia.
    varia = 1

    # The class constructor sets the variable with the parameter's value
    def __init__(self, val) :
        ExampleClass.varia = val
    
# Naming the variable is the most important aspect of the example because :
# Changing the assignment to self.varia = val would create an instance variable of the same name as the class's one.
# Changing the assignment to varia = val would operate on a method's local variable. (We strongly encourage you to test both of the above cases - this will make it easier for you to remember the difference.)

# This line prints the value of the ExampleClass.varia attribute.
# We use the value before the very first object of the class is instantiated.
print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
# The object has no instance variables, So this method returns empty dictionary.
print(example_object.__dict__)