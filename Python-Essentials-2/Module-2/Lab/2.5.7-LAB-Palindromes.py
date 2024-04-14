'''
Palindrome is a word which look the same when read forward and backward. 
For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

- asks the user for some text;
- checks whether the entered text is a palindrome, and prints the result.

Note:
- assume that an empty string isn't a palindrome;
- treat upper- and lower-case letters as equal;
- spaces are not taken into account during the check - treat them as non-existent;
- there are more than a few correct solutions - try to find more than one.

Test your code using the data we've provided.

Test Data :
1. Sample input:
    Ten animals I slam in a net

Sample output:
    It's a palindrome

2. Sample input:
    Eleven animals I slam in a net

Sample output:
    It's not a palindrome

'''
def is_palindrome(string):
    palindrome_ = ''
    if string == "" or string.isspace():
        print("It is not a Palindrome")
    else :
        for char in string :
            char = char.lower()
            if not char.isalpha() :
                continue
            else :
                palindrome_ += char

        if palindrome_ == palindrome_[::-1]:
            print("It is a Palindrome")
        else : 
            print("It is not a Palindrome")

string = input("Enter a string to check if it is a palindrome :")
is_palindrome(string)