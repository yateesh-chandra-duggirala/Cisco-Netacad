'''
Scenario :

Using one of the comparison operators in Python, write a simple two-line program that 
- takes the parameter n as input, which is an integer, and 
- prints False if n is less than 100, and
- True if n is greater than or equal to 100.

Don't create any if blocks (we're going to talk about them very soon). 
Test your code using the data we've provided for you.

-----------------------------------------------------------------------------------

Test Data :

1. Sample input: 55

Expected output: False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

2. Sample input: 99

Expected output: False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

3. Sample input: 100

Expected output: True

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

4. Sample input: 101

Expected output: True

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

5. Sample input: -5

Expected output: False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

6. Sample input: +123

Expected output: True


'''

n = int(input("Enter a number:"))

print(n>=100)