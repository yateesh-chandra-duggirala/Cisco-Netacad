# Random module helps us to generate pseudorandom numbers
# A Random Number generator takes a value called a seed calculates a random number based on it and produces new seed value
from random import random, seed, randrange, randint, choice, sample

# Define a seed - If we define a seed, The same random numbers will be generated everytime.
# seed(0)

# Display 5 random numbers
for i in range(5):
    print(random())

# randrange(end) method - This only prints random number until the range of 9.
print(randrange(9))

# randrange(beg, end) - This prints upto end, but excludes end number.
print(randrange(10, 15))

# randrange(beg, end, step) - This prints upto end, but excludes end number with some steps between them.
print(randrange(10, 20, 4))

# randint(left,  right)
print(randint(0, 1))

# choice(sequence) - chooses a random element from the input sequence and returns it.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))

# sample(sequence, number_of_elements) - creates a random list of number_of_elements.
print(sample(my_list, 5))

# It does not create the number more than the number of elements in the list.
# print(sample(my_list, 15)) - returns error
