digit_count=0
letter_count=0




user_input = input ("Please enter a string :-")
for ch in user_input:
    if ch.isdigit():
        digit_count=digit_count+1
    elif ch.isalpha():
        letter_count = letter_count +1

        #print("Please type something in alphanumeric manner")

print("Total count of digits :-",digit_count)
print("Total count of letters :-",letter_count)
