'''
Scenario :
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

- the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
- the histogram should be sent to a file with the same name as the input one, 
but with the suffix '.hist' (it should be concatenated to the original name)

Assuming that the input file contains just one line filled with:

samplefile.txt
cBabAa

the expected output should look as follows:

a -> 3
b -> 2
c -> 1

Output :
Tip: Use a lambda to change the sort order.

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
    stream = open(file_pth + ".hist" , 'wt')
    for word in sorted(dict_1, key= lambda x : dict_1[x], reverse=True):
        c = dict_1[word]
        if c > 0 :
            stream.write(word + "->" + str(c) + "\n")
    stream.close()

except IOError as e :
    print("Exception : ", strerror(e.strerror))