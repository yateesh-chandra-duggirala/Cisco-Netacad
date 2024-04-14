# Cipher was invented and used by the Caesar
# Every letter of the message is replaced by the nearest consequent. (A -> B), (B -> C). but for Z -> A.

# We've written it using the following assumptions:
# - it accepts Latin letters only (note: the Romans didn't use whitespaces or digits)
# - all letters of the message are in upper case (note: the Romans knew only capitals)

text = input("Enter a message :")
cipher = ''
for char in text : 
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z') :
        code = ord('A')
    cipher += chr(code)
print(cipher)
