import re

heroregex=re.compile(r'Batman|Superman')
mo=heroregex.search("My name is Batman")
print(mo.group())