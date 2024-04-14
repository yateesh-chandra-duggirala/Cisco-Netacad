# Let us import math module
from math import *

# Print the pi value according to the math module.
print(pi)

# sin(x) function returns the sine of the x
print(sin(pi/2))

# cos(x) function returns the cosine of the x
print(cos(pi/2))

# tan(x) function returns the tangent of the x
print(tan(pi/2))

ad = 90
ar = radians(ad)
ad = degrees(ar)
    
print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

# e is a constant with a value that is an approximation of euler's number (e)
print(pow(e, 1))

# exp(x) is finding the value of e to the power of x.
# log(x) is the natural logarithmic value of x.
print(exp(log(4)))

# log(x, b) is the logarithm of x to the base b
print(log(2, 2))

# log10(x) is just like log(x, 10) - A decimal Logarithm
print(log10(5))

# log2(x) is just like log(x, 2) - A Binary Logarithm
print(log2(4))

# pow(x, y) - finds the value of x power of y.
print(pow(25, 0.5))


# ceil(x) the ceiling value or the next larger integer value of the float number
print(ceil(26.3))

# floor(x) the floor value or the next smaller integer value of the float number
print(floor(2.4))
print(floor(-2.4))

# factorial(x) - factorial value of the x in the number
print(factorial(4))

# trunc(x) - Remove the decimal part of the integer
print(trunc(-1.4))
print(trunc(3.5))

# hypot(x, y) - Hypotenuse of the right angle with x, y as side values
print(hypot(3,4))

# sqrt() - Returns the square root of the value
print(sqrt(16))