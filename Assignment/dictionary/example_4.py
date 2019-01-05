d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key_value=int(input("Please enter a key value please :- "))

def key_finding(value):
    if value in d:
        print("Key value exist in dictionary ")
        print("Value corresponding to key is :-",d[key_value])
    else:
        print("Key is not here :- !!!")

key_finding(key_value)