from os import strerror

try :
    character_counter = line_counter = 0
    stream = open('D:/cisco-practice/Python-Essentials-2/Module-4/Practice/text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line :
            print(char, end = '')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file : ", character_counter)
    print("Lines in file : ", line_counter)

except IOError as ex:
    print("I/O Error occured : ", strerror(ex.errno))