my_string=input("Please enter your string :-")
count=0

for ch in my_string:
    print(ch)
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
        count=count+1

print("Total number of vowel count will be :-", count)