my_string=input("Please enter a string :- ")
count={ }


for characters in my_string:
    count.setdefault(characters,0)
    count[characters]=count[characters]+1
print(count)