'''
Scenario:
Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab (3.1.2.10) and create a better, upgraded (pretty) vowel eater! 

Write a program that uses:
- a for loop;
- the concept of conditional execution (if-elif-else)
- the continue statement.

Your program must:
-ask the user to enter a word;
- use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
- use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
- assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
-
Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the word_without_vowels variable.

Test your program with the data we've provided for you.

-----------------------------------------------------------------------------------

Test data:

1. Sample input: Gregory

Expected output:
GRGRY

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

2. Sample input: abstemious

Expected output:
BSTMS

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

3. Sample input: IOUEA

Expected output:

'''

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the userWord variable.
user_word = input("Enter the word:")


for letter in user_word:
    if letter.upper() in ['A','I','U','E','O']:
        continue
    
    word_without_vowels += letter.upper()
    
print(word_without_vowels)