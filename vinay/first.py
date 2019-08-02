import sys

while True:
    response=input("Please enter exit if you need to exit :- ")
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
