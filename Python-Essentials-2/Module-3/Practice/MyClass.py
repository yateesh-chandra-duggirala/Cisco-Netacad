# Define a simple Class MyClass.
class MyClass:
    pass

# Create an object.
obj = MyClass()

# Fill the object with some attributes.
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

# Define a function named 'incIntsI" and get the object of any class
def incIntsI(obj):
    # Scan the __dict__ attribute looking for all attribute names.
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            # increment the value by 1, if it is an integer and starts with 'i' letter
            # isinstance() is method used to check if the value is of integer type
            if isinstance(val, int):
                # setattr() function takes three params : an object, property name, property new value
                setattr(obj, name, val + 1)


print(obj.__dict__)
# {'a' : 1 , 'b' : 2, 'i' : 3, 'ireal' : 3.5, 'integer' : 4, 'z' : 5}
incIntsI(obj)
# {'a' : 1 , 'b' : 2, 'i' : 4, 'ireal' : 3.5, 'integer' : 5, 'z' : 5}
print(obj.__dict__)
