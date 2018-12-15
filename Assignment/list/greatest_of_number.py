number_list=[ ]

keep_going='y'

while keep_going.lower()=='y':
    number=int(input("Please enter a number :- "))
    number_list.append(number)

    keep_going=input("Please enter y to continue :- ")

number_list.sort()
length=len(number_list)

print("Greatest number will be :-", number_list[length-1])