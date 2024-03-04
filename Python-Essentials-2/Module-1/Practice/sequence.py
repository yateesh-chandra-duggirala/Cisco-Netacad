# When we want to use the methods from the module and our own function together.
from math import sin, pi

# Printing the sin of value of pi / 2.
print(sin(pi/2))

# Let us try to redefine the pi value.
pi = 3.14

# When we Redefine the function, It gets superseded.
def sin(x):
    if 2 * x == pi:
        return 0.99999
    else:
        return 1

# If we print the value, It is not 1.0 as per the module value. Instead, It is 0.999 according to the function
print(sin(pi/2))