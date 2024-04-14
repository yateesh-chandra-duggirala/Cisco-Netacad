'''
Scenario :
Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air.
Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.

Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"

Write a program that utilizes the concept of conditional execution, takes a string as input, and:

- prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
- prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
- prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

-----------------------------------------------------------------------------------

Test Data:

1. Sample input: spathiphyllum

Expected output: No, I want a big Spathiphyllum!

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

2. Sample input: pelargonium

Expected output: Spathiphyllum! Not pelargonium!

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

3. Sample input: Spathiphyllum

Expected output: Yes - Spathiphyllum is the best plant ever!

'''
str = input("Enter the name of a plant : ")

if(str == "Spathiphyllum"):
    print("Yes - Spathiphyllum is the best plant ever!")
elif(str == "spathiphyllum"):
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not "+str+"!")