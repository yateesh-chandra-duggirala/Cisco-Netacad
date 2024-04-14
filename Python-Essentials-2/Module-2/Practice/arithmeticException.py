try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")


# Something has changed in it - we've replaced ZeroDivisionError with ArithmeticError.
# ArithmeticError is a general class including (among others) the ZeroDivisionError exception.
# Thus, the code's output remains unchanged. Test it.
# This also means that replacing the exception's name with either Exception or BaseException 
# won't change the program's behavior.


try:
    y = 1 / 0
except ZeroDivisionError:           # Concrete Branch
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")    # General Branch

print("THE END.")
    

# each exception raised falls into the first matching branch;
# the matching branch doesn't have to specify the same exception exactly – 
# it's enough that the exception is more general (more abstract) than the raised one.


try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")


# The exception is the same, but the more general exception is now listed first – 
# it will catch all zero divisions too.
#  It also means that there's no chance that any exception hits the ZeroDivisionError branch. 
# This branch is now completely unreachable.

'''
Rules :
- the order of the branches matters!
- don't put more general exceptions before more concrete ones;
- this will make the latter one unreachable and useless;
- moreover, it will make your code messy and inconsistent;
- Python won't generate any error messages regarding this issue.
'''

# Also If we want to add more than one exception in a single block, We can follow : except(exception1, exception2)