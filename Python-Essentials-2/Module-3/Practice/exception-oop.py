def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError :
        print("Division Failed")
        return None
    else :
        print("Everything went fine")
        return n

print(reciprocal(2))
print(reciprocal(0))