# A module is a kind of container filled with functions.
# A package is a kind of container filled with modules.
import module1

# Since the Module 2 contains the module 1 and it is imported, The module 2 is imported and executes,
# The initialization takes place only once, when the first import occurs.
# So the assignments done by the module aren't repeated unnecessarily.
import module2

# If we print the imported module1, The print statement from that module, prints the name of the module(module1)
# Let us import the test_module
import test_module

# Access the counter variable from the test_module.
print(test_module.counter)