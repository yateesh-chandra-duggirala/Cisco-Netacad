from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try :
    bf = open("D:/cisco-practice/Python-Essentials-2/Module-4/Practice/text_bin.bin", "wb")
    bf.write(data)
    bf.close()
except IOError as ex :
    print(strerror(ex.errno))