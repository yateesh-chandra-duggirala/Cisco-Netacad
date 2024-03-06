try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

x = '\''
print(len(x))

print(3 * 'abc' + 'xyz')

print('Mike' > "Mikey")

print(float("1, 3"))

