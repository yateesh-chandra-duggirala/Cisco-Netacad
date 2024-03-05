''' 
You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:
- it should accept exactly one argument - a string;
- it should return a list of words created from the string, divided in the places where the string contains whitespaces;
- if the string is empty, the function should return an empty list;
- its name should be mysplit()
Use the template in the editor. Test your code carefully. 

Expected output
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[]

'''

def mysplit(strng):

    list1 = []
    
    if strng.isspace() or strng == "":
        return list1
    
    else :
        string_char = ''
        for character in strng:
            if character != " ":
                string_char += character
            else :
                if string_char != '':
                    list1.append(string_char)
                    string_char = ''
        if string_char != '':
            list1.append(string_char)
        return list1
    

print(mysplit("To be or not to be, this is a question"))
print(mysplit("To be or not to be,this is a question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


