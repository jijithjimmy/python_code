my_string=input("Please enter a string :-")

count={ }

for ch in my_string:
    count.setdefault(ch,0)
    count[ch]=count[ch]+1
    print(count)

