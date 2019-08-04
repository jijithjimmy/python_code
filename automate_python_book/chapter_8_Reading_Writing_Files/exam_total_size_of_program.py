import os

total_size=0

for files in os.listdir('/Users/jjimmy/Desktop'):
    #print(files)   -->working
    total_size=total_size+os.path.getsize(os.path.join('/Users/jjimmy/Desktop',files))

print(total_size)