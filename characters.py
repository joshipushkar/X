character="A"
if ord(character) >=97 and ord(character)<=122:
    print("Small letter",character)
elif ord(character) >=65 and ord(character)<=90:
    print("Cap Letter",character)
elif ord(character) >=48 and  ord(character)<=57:
    print("digits")
else:
    print("Special Character")