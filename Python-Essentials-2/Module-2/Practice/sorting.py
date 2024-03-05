# Sorting happens accordingly in the Strings 
greek = ['omega', 'alpha', 'pi', 'gamma']

# Method - 1 : using sorted() function
# The method takes one argument and returns a new list filled with sorted elements from the list.
# The original list remains untouched.

greek_sorted = sorted(greek)

print(greek)
print(greek_sorted)

# Method - 2 : using sort() method
# Here no new list is created

greek.sort()
print(greek)