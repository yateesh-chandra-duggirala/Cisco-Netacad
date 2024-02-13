# The platform module lets you access underlying platform's data. i.e., hardware, OS, Interpreter version Information.
# There is a function that can show you all the underlying layers in one glance, named platform, too
# platform(aliased = False, terse = False)
# aliased - When set to True, it may cause the function to present alternative underlying layer names instead of common ones.
# terse - When set to True, It may convince the function to present a briefer form of the result
from platform import platform, machine, processor
print(platform())
print(platform(1))
print(platform(0, 1))

# machine() function lets us know the generic name of the processor which runs the OS Together with Python and the code
print(machine())

# Processor() function returns a string filled with the real processor name
print(processor())