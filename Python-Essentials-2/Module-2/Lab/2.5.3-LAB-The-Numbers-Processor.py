# User needs to input a line filled with numbers, and to process them easily. 
# Note: the routine input() function, combined together with the int() or float() functions, is unsuitable for this purpose.

# The processing will be extremely easy – we want the numbers entered from the user to be summed.
# Using list comprehension may make the code slimmer. You can do that if you want.
# Also, If the user inputs spaces, it displays Bogus Result, Hence that is also fixed here.

string = input("Enter the numbers you want to sum by just seperating with spaces : ")
list1 = string.split()
total = 0
try :
    for num in list1 :
        total += float(num)
    if not total :
        print("No result")
    else :
        print(total)

except :
    print(num , "not a number")