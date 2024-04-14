from os import strerror

# stream = open('D:/cisco-practice/Python-Essentials-2/Module-4/Practice/text.txt', 'rt')
# char = stream.read(5)
# print(char)
# stream.close()

try:
    counter = 0
    stream = open('D:/cisco-practice/Python-Essentials-2/Module-4/Practice/text.txt', 'rt')
    # read(n) - reads the content upto nth character
    char = stream.read(1)
    while char != '':
        print(char, end = '')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("Characters in file : ", counter)

except IOError as ex :
    print("I/O error occured :", strerror(ex.errno))