def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else :
            n = p + pp
            p, pp = pp, n
            yield n

fib = list(fibonacci(10))

print(fib)
