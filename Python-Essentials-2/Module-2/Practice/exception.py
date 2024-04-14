# 1. Raises Value Error Exception
'''
import math
x = float(input("Enter x: "))
y = math.sqrt(x)
print("The square root of", x, "equals to", y)
'''

# Scenario 1 : the execution may fail just because user might have entered any float value.
# Scenario 2 : the execution may fail when it gets a negative argument into it.

# 2. Raises ZeroDivisionError :
'''
value = 1
value /= 0
'''
#3. Raises IndexError :
'''
my_list = []
x = my_list[0]
'''

try:
    first_number = int(input("Enter first number : "))
    second_number = int(input("Enter second number : "))
    print(first_number/second_number)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("\nOh dear, something went wrong...")

print("THE END.")
    
# Except block follows a sequence after try
# Atleast one except block should be there when we want to use the try
# More than one anonymous except branch should not be there after named except block.