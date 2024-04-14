# Converting a ciphered text to plain text, Just like a vice versa for the Encryption of message.
cipher = input('Enter encrypted Message :')
plain = ''
for char in cipher :
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('A')
    plain += chr(code)

print(plain)