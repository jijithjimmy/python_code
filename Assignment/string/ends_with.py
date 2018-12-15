input_string=input("Please enter a string :-")

if len(input_string) <= 3:
    print("String remains unchanged and it is :-",input_string)


elif len(input_string) > 3 and input_string.endswith('ing'):
    new_string=input_string + 'ly'
    print(new_string)

else:
    new_string=input_string+'ing'
    print(new_string)












