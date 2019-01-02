import re
batregex=re.compile(r'Bat(wo)?man')
mo=batregex.search('My favourite cartoon is :- Batman')
mo1=batregex.search('My favourie cartoon is :- Batwoman')
mo2=batregex.search('My favourie cartoon is :- Batwowowowman')
print(mo.group())
print(mo1.group())
if mo2==None:
    print("FOUND!!!")