def isPhoneNumber(text):
    if len(text) != 12 :
        return False
    for counter in range(0,3):
        if not text[counter].isdecimal():
            return False
    if text[3] != '-':
        return False
    for counter in range(4,7):
        if not text[counter].isdecimal():
            return False
    if text[7] != '-':
        return False
    for counter in range(8,12):
        if not text[counter].isdecimal():
            return False
    return True


number=input("Please enter a number :-")
print(isPhoneNumber(number))

====================
def isPhoneNumber(text):
    if len(text) != 12 :
        return False
    for counter in range(0,3):
        if not text[counter].isdecimal():
            return False
    if text[3] != '-':
        return False
    for counter in range(4,7):
        if not text[counter].isdecimal():
            return False
    if text[7] != '-':
        return False
    for counter in range(8,12):
        if not text[counter].isdecimal():
            return False
    return True

message= "Call me at 123-456-789 around any time . My alternate number will be 000-123-097"
foundnumber=False

for counter in range(len(message)):
    chunk=message[counter:(counter+12)]

    if isPhoneNumber(chunk):
        print("Phone number found :-", chunk)
        foundnumber=True
if not foundnumber:
    print("Phone number not found !!!")

======================

import re
phoneNumberregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumberregex.search('My phone number is :- 123-456-7890')
print("Phone number found :- ", mo.group())

=======================

import re
phonenumregex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo=phonenumregex.search('My mobile number is 123-345-5678')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))

======================

import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

=====================

import re
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

=====================
import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1=batRegex.search('Batmobile lost a wheel')
print(mo1.group())
print(mo1.group(1))

====================
