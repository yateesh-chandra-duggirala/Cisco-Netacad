# The platform module lets you access underlying platform's data. i.e., hardware, OS, Interpreter version Information.
# There is a function that can show you all the underlying layers in one glance, named platform, too
# platform(aliased = False, terse = False)  - In my case, Windows - 10
# aliased - When set to True, it may cause the function to present alternative underlying layer names instead of common ones.
# terse - When set to True, It may convince the function to present a briefer form of the result
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
print(platform())
print(platform(1))
print(platform(0, 1))

# machine() function lets us know the generic name of the processor which runs the OS Together with Python and the code
print(machine())

# Processor() function returns a string filled with the real processor name - Intel64 family
print(processor())

# system() returns the generic OS name as a string. - In my case, It is Windows
print(system())

# version() function returns the version of the OS - In my case, It is Windows
print(version())

# python_implementation() returns a string denoting the python implementation. - Returns the CPython
print(python_implementation())

# python_version_tuple - returns the three element tuple filled with a) major part of Python's Version(3). b) minor part(11). c) patch level number(5).
print(python_version_tuple())

# print the version in the format of string instead of tuple
print("python version ", end = ": ")
for v in python_version_tuple():
    print(v, end = '.')