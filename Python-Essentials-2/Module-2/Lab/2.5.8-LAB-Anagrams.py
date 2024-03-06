'''
An Anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once.
For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:
    - asks the user for two separate texts;
    - checks whether, the entered texts are anagrams and prints the result.


Note:
    - assume that two empty strings are not anagrams;
    - treat upper- and lower-case letters as equal;
    - spaces are not taken into account during the check treat them as non-existent

Test your code using the data we've provided.

1. Sample input:
    Listen
    Silent

   Sample output:
    Anagrams


2. Sample input:
    modern
    norman

   Sample output:
    Not anagrams
'''

def is_anagram(string1, string2):

    # Check that the strings should not contain empty strings
    if len(string1) >= 1 and len(string2) >= 1 :

        # Create a list for string 1 with their characters in a sorted order
        sorted_string1 = sorted(string1.lower().replace(" ", ""))

        # Create a list for string 2 with their characters in a sorted order
        sorted_string2 = sorted(string2.lower().replace(" ", ""))

        # Check if both the lists of strings are same.
        if(sorted_string1 == sorted_string2):
            print("Anagrams")
        else :
            print("Not Anagrams")
    else :
        print("Not Anagrams")

print("****Enter the strings to check if they are Anagrams or not****")
string1 = input("Enter first String : ")
string2 = input("Enter second String : ")
is_anagram(string1, string2)