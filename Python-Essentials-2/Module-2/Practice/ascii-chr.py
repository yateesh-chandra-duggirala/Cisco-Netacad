# ord() method is used to know a specific character's ASCII/ UNICODE code point value.
char_1 = 'a'
char_2 = 'A'
char_3 = ' '
alpha = 'α'                 # Greek Alpha
polish_alphabet = 'ę'       # Polish Alphabet

print(ord(char_1))
print(ord(char_2))
print(ord(char_3))
print(ord(alpha))
print(ord(polish_alphabet))

# chr() method is used to convert code point to character
print(chr(97))
print(chr(201))
print(chr(32))

print(f'9 : {chr(ord("9"))}')
print(f'9 : {ord(chr(9))}')

