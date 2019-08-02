cats_name=[ ]

while True:
    name=input("Please enter cats name :- ")
    if name == '':
        print("You have to enter something!!! Exiting from program!!!")
        break

    cats_name.append(name)


#print(cats_name)
for counter in cats_name:
    print(counter)