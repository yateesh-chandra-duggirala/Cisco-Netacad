'''
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. 
Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and 
all non-alphabetical characters should remain untouched.

Your task is to write a program which:
- asks the user for one line of text to encrypt;
- asks the user for a shift value (an integer number from the range 1..25 - 
    note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
- prints out the encoded text.
Test your code using the data we've provided.

1. Sample input:
    abcxyzABCxyz 123
    2

   Sample output:    cdezabCDEzab 123

2. Sample input:
    The die is cast
    25

    Sample output: Sgd chd hr bzrs
'''

plain_text = input("Enter the message to encrypt :")
shift_value = int(input("Enter the shift value : "))
cipher = ''
for char in plain_text:
    if char.isupper():
        code = ord(char) + shift_value
        if code > ord('Z'):
            code = ord('A') + ((code - ord('A')) % 26)
        cipher += chr(code)
    elif char.islower():
        code = ord(char) + shift_value
        if code > ord('z'):
            code = ord('a') + ((code - ord('a')) % 26)
        cipher += chr(code)
    else :
        cipher += char

print(cipher)