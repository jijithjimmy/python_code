def isPhoneNumber(text):
    if len(text) != 12 :
        return False
    for counter in range(0,3):
        if not text[counter].isdecimal():
            return False
    if text[3] != '-':
        return False
    for counter in range(4,7):
        if not text[counter].isdecimal():
            return False
    if text[7] != '-':
        return False
    for counter in range(8,12):
        if not text[counter].isdecimal():
            return False
    return True


number=input("Please enter a number :-")
print(isPhoneNumber(number))