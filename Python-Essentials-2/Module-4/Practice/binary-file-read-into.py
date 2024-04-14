from os import strerror
data = bytearray(12)

try :
    binary_file =  open("D:/cisco-practice/Python-Essentials-2/Module-4/Practice/text_bin.bin", "rb")
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end = ' ')
except IOError as e :
    print("I/O error occured : ", strerror(e.errno))
