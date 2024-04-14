'''
Scenario :

As you surely know, due to some astronomical reasons, years may be leap or common. 
The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
-if the year number isn't divisible by four, it's a common year;
-otherwise, if the year number isn't divisible by 100, it's a leap year;
-otherwise, if the year number isn't divisible by 400, it's a common year;
-otherwise, it's a leap year.

The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

Test your code using the data we've provided.

-----------------------------------------------------------------------------------

Test Data:

1. Sample input: 2000

Expected output: Leap year

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

2. Sample input: 2015

Expected output: Common year

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

3. Sample input: 1999

Expected output: Common year

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

4. Sample input: 1996

Expected output: Leap year

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

5. Sample input: 1580

Expected output: Not within the Gregorian calendar period
'''

year = int(input("Enter a year: "))

if year > 1582:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Common Year")
else:
    print("Not Within the Gregorian calendar period")
