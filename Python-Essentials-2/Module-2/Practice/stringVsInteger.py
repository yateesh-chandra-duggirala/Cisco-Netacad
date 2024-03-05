# An Integer or float can be directly converted into String by type casting using str() function.
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

# We can also reverse the conversion (from string to integer) only when the string is valid number.
# Or else, It would result in a Value Error.
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)