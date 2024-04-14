# Build a list_1 with values iterating from 0 to 4
list_1 = [x for x in range(5)]

# build a list 2 from each item by raising to each item from list using map() function.
list_2 = list(map(lambda x: 2 ** x, list_1))

# Print the list_2
print(list_2)

# Now Use map() function again to make use of the generator it returns and to directly print all the values it delivers;
# We have engaged the second lambda here - it just squares each element from the list_2.
for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()