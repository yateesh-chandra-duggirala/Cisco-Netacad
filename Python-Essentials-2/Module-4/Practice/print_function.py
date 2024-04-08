# Define a function with two parameters.
# The First parameter - a list of arguments for which we want the results to be printed.
# The Second Parameter - Function that should be invoked as many times the number of values that are collected inside the parameter
def print_function(args, fun):
    for x in args:
        print('f(', x, ') \t = \t', fun(x), sep = '')

# Instead of writing this function, We can use lamba function
'''
def poly(x):
    return 2 * x**2 - 4 * x + 2
'''

print_function([x for x in range(-2, 3)], lambda x : 2 * x**2 - 4*x + 2)