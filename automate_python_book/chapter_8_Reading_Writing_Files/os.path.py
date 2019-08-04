import os

#print(os.path.abspath('.'))

#ans = os.path.isabs('.')

ans = os.path.isabs(os.path.abspath('.'))
if ans == False:
    print("Not an absolute path")
else:
    print("Absolute path")