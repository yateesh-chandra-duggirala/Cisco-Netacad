# A Namespace is a space in which some names exist and the names do not conflict with Each other
import math

# Define the sin function
def sin(x):
    if 2 * x == pi:
        return 0.9999
    else:
        return 1

pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))