'''
Let's play a game. We will give you two strings: 
one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: 
are the characters comprising the first string hidden inside the second string?

For example:

- if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
- if the second string is "vcxzxdcybfdstbywuefsas", the answer is no 
    (as the letters "d", "o", or "g" don't appear in this order)

Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
Test your code using the data we've provided.

1. Sample input:
    donor
    Nabucodonosor

   Sample output:
    Yes

2. Sample input:
    donut
    Nabucodonosor

   Sample output:
    No
'''

# Create a word variable that stores the word you want to search.
word = input("Enter a string to check if it is present in target string : ").upper()

# Create a target variable that stores the target string and starts searching the word.
target = input("Enter the target string : ").upper()

# create a flag
found = True

# Initial Index set to 0
start = 0

for char in word :

    # Create a pos variable that finds the beginning character from the string and stores its index from the target
    pos = target.find(char, start)
    if (pos < 0):
        
        # Set the flag to False and exit from the loop
        found = False
        break
    # Increase the index
    start = pos + 1

if found :
    print("Yes")
else : 
    print("No")

