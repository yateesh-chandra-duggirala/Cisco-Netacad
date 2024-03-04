# min() function finds the minimum element of the sequence passed as an argument
# There is a single condition, That it should not be empty.
print(min("aAbByYzZ"))

t = 'The Knights Who say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# max() function finds the maximum element of the sequence passed as an argument.
print(max("aAbByYzZ"))

t = 'The Knights Who say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# index() method is used to return the first index of a specific character from the string mentioned in the argument.
# If the element mentioned in the argument is not present in the string, It returns "Value Error".
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# The list() function takes an argument and creates a new list containing all the characters from the string.
# The set() function takes an argument and creates a new set containing all the characters from the string by removing its recurring occurences.
print(list("YateeshChandra"))
print(set("YateeshChandra"))

# The count() method is used to print the number of times a character occured from the string. returns 0 if not found
print("yateesh".count("e"))