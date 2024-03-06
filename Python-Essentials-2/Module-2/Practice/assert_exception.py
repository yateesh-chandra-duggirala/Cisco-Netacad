# if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, 
# or any other value different than None, it won't do anything else;
# otherwise, it automatically and immediately raises an exception named AssertionError 
# (in this case, we say that the assertion has failed)

# you may want to put it into your code where you want to be absolutely safe from evidently wrong data, 
# and where you aren't absolutely sure that the data has been carefully examined before 
# (e.g., inside a function used by someone else)
# raising an AssertionError exception secures your code from producing invalid results, and clearly shows the nature of the failure;
# assertions don't supersede exceptions or validate the data – they are their supplements.
import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)