import os
filenames=['accounts.txt','details.csv','invite.png']
for files in filenames:
    print(os.path.join('/Users/jjimmy/Desktop/workspace/python_code/TRASH',files))

=====
import os
print(os.getcwd())

=======

import os
os.chdir('/Users/jjimmy/Desktop/workspace/')
print(os.getcwd())
========
import os
os.makedirs('/Users/jjimmy/Desktop/workspace/python_code/TRASH/jenita.txt')   # will create a file/folder
=======

import os
print(os.path.abspath('.'))

=======

os.path.isabs('.')
os.path.isabs(os.path.abspath('.'))
======
import os
print(os.path.relpath('/Users/jjimmy/Desktop/workspace/python_code/TRASH/chumma.py','/Users/jjimmy/Desktop/'))

========

import os
print(os.path.dirname('/Users/jjimmy/Desktop/workspace/python_code/TRASH/chumma_learning.py'))
print(os.path.basename('/Users/jjimmy/Desktop/workspace/python_code/TRASH/chumma_learning.py'))

========

import os
print(os.path.exists('/Users/jjimmy/Desktop/workspace/python_code/TRASH/chumma_learning.py'))
print(os.path.exists('/Users/jjimmy/Desktop/workspace/python_code/TRASH/chumma'))
print(os.path.isfile('/Users/jjimmy/Desktop/workspace/python_code/TRASH/chumma_learning.py'))
print(os.path.isdir('/Users/jjimmy/Desktop/workspace/python_code/TRASH/'))

=======
import os
print(os.path.getsize('/Users/jjimmy/Desktop/workspace/python_code/TRASH/'))
print(os.listdir('/Users/jjimmy/Desktop/workspace/python_code/'))

======
import os
total_size=0

for filenames in os.listdir('/Users/jjimmy/Desktop/workspace/python_code/'):
    #total_size=total_size+os.path.getsize(os.path.join('/Users/jjimmy/Desktop/workspace/python_code/',filenames))
    if not os.path.isdir(os.path.join('/Users/jjimmy/Desktop/workspace/python_code/',filenames)):
        total_size=total_size+os.path.getsize(os.path.join('/Users/jjimmy/Desktop/workspace/python_code/',filenames))


print(total_size)


=======