'''
The standard named IBAN (International Bank Account Number) provides a simple and fairly reliable method 
for validating account numbers against simple typos that can occur during rewriting of the number,
for example, from paper documents, like invoices or bills, into computers.

An IBAN-compliant account number consists of:

- A two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
- two check digits used to perform the validity checks - fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
- the actual account number (up to 30 alphanumeric characters - the length of that part depends on the country)

The standard says that validation requires the following steps (according to Wikipedia):

(step 1) Check that the total IBAN length is correct as per the country (this program won't do that, but you can modify the code to meet this requirement if you wish; 
        note: you have to teach the code all the lengths used in Europe)
(step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
(step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35;
(step 4) Interpret the string as a decimal integer and compute the remainder of that number by modulo-dividing it by 97; 
        If the remainder is 1, the check digit test is passed and the IBAN might be valid.

TEST DATA : 
(all these numbers are valid - you can invalidate them by changing any character).

British: GB72 HBZU 7006 7212 1253 00
French: FR76 30003 03620 00020216907 50
German: DE02100100100152517108
'''

# IBAN Validator
iban = input("Enter IBAN :")
iban = iban.replace(' ', '')

if not iban.isalnum():
    print("You have entered invalid characters")
elif len(iban) < 15 :
    print("IBAN is too short")
elif len(iban) > 31 :
    print("IBAN is too long")
else : 
    iban = (iban[4:] + iban[:4]).upper()
    iban_2 = ''
    for char in iban : 
        if char.isdigit():
            iban_2 += char
        else :
            iban_2 += str(10 + ord(char) - ord('A'))
    iban_2 = int(iban_2)
    if iban_2 % 97 == 1:
        print("The IBAN Value is valid")
    else :
        print("The IBAN value is invalid")
