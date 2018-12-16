birthday_details={'jijith':'18 june','jitha':'22 july','jenIta':'4 april'}
#print(birthday_details)

keep_going='y'

while keep_going.lower()=='y':
    name=input("Please enter a name :- ")
    name.lower()

    if name in birthday_details :
        print("{} birthday is at :-".format(name))
        print(birthday_details[name])
    else:
        print("Name doesnt exist in dictionary ")
        date=input("Please enter the details of birthday :- ")
        birthday_details[name]=date

    keep_going=input("Please enter y if you need to continue further :- ")
