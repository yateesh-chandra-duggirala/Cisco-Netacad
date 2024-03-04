# Initialize the pi value
pi = 3.14

# Define the function
def sin(x):
    if 2 * x == pi:
        return 0.99999
    else:
        return 1

# print the value.
print(sin(pi/2))

# Let us consider the sin and pi from the module math inorder to supersede
from math import sin, pi

# Printing the sin of value of pi / 2 after redeclaration.
print(sin(pi/2))