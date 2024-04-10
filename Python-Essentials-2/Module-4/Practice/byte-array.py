data = bytearray(10)
print(len(data))

for i in range(len(data)):
    data[i] = 10 - i

for i in data:
    print(hex(i))