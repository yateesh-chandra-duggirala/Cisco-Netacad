from os import strerror

try :
    stream = open("D:/cisco-practice/Python-Essentials-2/Module-4/Practice/newtxt.txt", 'wt')
    for i in range(10):
        s = "Line #" + str(i+1) + "\n"
        print(s)
        stream.write(s)
    stream.close()
except IOError as ex :
    print(strerror(ex.errno))