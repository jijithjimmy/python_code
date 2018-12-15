input_string=input("Please enter a string :-")
total_count=len(input_string)

if len(input_string)<2:
    print("String should be minimum 2 characters!!! Please try again !!!")
else:
    first_slice = input_string[0:2]
    last_slice = input_string[(total_count - 2):(total_count + 1)]
    final_string = first_slice + last_slice
    print("Final string will be :-", final_string)
