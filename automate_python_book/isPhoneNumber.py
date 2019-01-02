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

import re
phonenumberregex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo=phonenumberregex.search('My number is :- 345-6789')
print(mo.group())

======================

import re
batregex=re.compile(r'Bat(wo)?man')
mo=batregex.search('My favourite cartoon is :- Batman')
mo1=batregex.search('My favourie cartoon is :- Batwoman')
mo2=batregex.search('My favourie cartoon is :- Batwowowowman')
print(mo.group())
print(mo1.group())
if mo2==None:
    print("FOUND!!!")

=====================

Matching Zero or More with the Star

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

===================

Matching One or More with the Plus

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
if mo3 == None:
    print("Nothing is found !!!")

====================

Matching Specific Repetitions with Curly Brackets

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
'HaHaHa'
mo2 = haRegex.search('Ha')
mo2 == None
True


====================

greedy and nongreedy matching

Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible.
The non- greedy version of the curly brackets, which matches the shortest string pos- sible,
has the closing curly bracket followed by a question mark.

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2=nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())


======================

the findall() method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']   # a list of string is got as an output


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '1122'), ('212', '555', '0000')]  # a list of tuples , with each matched items

=====================



