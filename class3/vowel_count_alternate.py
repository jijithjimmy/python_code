my_string=input("Please enter your string :-")
count=0

for ch in my_string:
    if ch in 'aeiouAEIOU':
        count=count+1

print("Total vowel count is :-", count)