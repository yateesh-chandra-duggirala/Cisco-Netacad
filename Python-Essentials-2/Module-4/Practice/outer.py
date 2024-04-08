def outer(par):
    loc = par

    # The inner function returns the value of the variable accessible inside scope,
    # As inner() can use any of the entities at the disposal of outer()
    def inner():
        return loc
    return inner

# The outer() function returns the inner() function itself.
# More precisely, It return a copy of the inner() function, the one which was frozen at the moment of the outer()'s invocation
# The frozen function contains its full enviroment, including the state of all local variables.
# This also means the value of loc is successfully retained, although outer() ceased to exist a long time ago.

var = 1
fun = outer(var)

# The function returned during the outer() invocation is a closure.
# A closure has to be invoked in exactly the same way in which it has been declared.
print(fun())
    