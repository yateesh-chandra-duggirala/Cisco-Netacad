two = lambda : 2
sqr = lambda x : x * x
pwr = lambda x, y : x ** y

for a in range(0, 5):
    print(sqr(a), end = ' ')
    print(pwr(a, two()))