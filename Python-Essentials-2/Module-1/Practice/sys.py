# sys module helps us to track the system
import sys

# path helps us to find the path for the system in python.
for p in sys.path:
    # The folder in which the execution starts will be placed at the first.
    print(p)

# We can also add our existing folder to our path\
from sys import path
path.append('..\\modules')