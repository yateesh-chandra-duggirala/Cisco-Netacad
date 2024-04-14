from os import strerror

try :
    binary_file = open("D:/cisco-practice/Python-Essentials-2/Module-4/Practice/text_bin.bin", "rb")
    data = bytearray(binary_file.read(1))
    binary_file.close()

    for b in data :
        print(hex(b), end = ' ')

except IOError as e :
    print(strerror(e.errno))