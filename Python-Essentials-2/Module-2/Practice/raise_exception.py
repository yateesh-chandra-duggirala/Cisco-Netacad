def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise   # raise is a keyword that would help us to raise an error


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

# The output will raise ZeroDivisionError twice. One, When the function is called and the other outside the function.