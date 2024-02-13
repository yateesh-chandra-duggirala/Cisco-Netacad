# dir() function is used to list out all the names through particular module.
# For that we have to import that module first
import math

# If we print the dir() then all the entities will be fetched from the module
for name in dir(math):
    print(name, end = "\t\t")