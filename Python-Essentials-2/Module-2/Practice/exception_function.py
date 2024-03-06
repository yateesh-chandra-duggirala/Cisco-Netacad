# Exceptions can be raised inside and outside the function

# a. Inside the function
def bad_fun(n):
    try:
        return (1 / n)
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(2)

print("THE END.")

# b. Outside the function

def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

