import os

myfiles=['school','college','job']

for counter in myfiles:
    print(os.path.join('/home/jijith',counter))