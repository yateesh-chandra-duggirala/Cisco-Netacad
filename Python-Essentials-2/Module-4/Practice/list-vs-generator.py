the_list = [1 if x %2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))


print(type(the_list))
print(type(the_generator))
print("\n")

for v in the_list:
    print(v, end = ' ')
print("\n")

for v in the_generator:
    print(v, end = " ")
print("\n")