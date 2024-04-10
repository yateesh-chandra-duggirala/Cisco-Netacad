'''
Scenario :
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. 
Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

- asks the user for the input file's name;
- reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
- prints a simple histogram in alphabetical order (only non-zero counts should be presented)

Create a test file for the code, and check if your histogram contains valid results.
Assuming that the test file contains just one line filled with:

samplefile.txt
aBc

Expected Output :
a -> 1
b -> 1
c -> 1


Tip: We think that a dictionary is a perfect data collection medium for storing the counts. 
The letters may be keys while the counters can be values.
'''

from os import strerror

file_pth = input("Enter the File Path :")

try :
    dict_1 = {}
    stream_file = open(file_pth, 'rt')
    file_read = stream_file.read()
    stream_file.close()
    for i in file_read :
        i = i.lower()
        if i == " ":
            continue
        elif i in dict_1.keys():
            dict_1[i] += 1
        else:
            dict_1[i] = 1
    
    for word in sorted(dict_1):
        print(word , "->", dict_1[word] )

except IOError as e :
    print("Exception : ", strerror(e.strerror))