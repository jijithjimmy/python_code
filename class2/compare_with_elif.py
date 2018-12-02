first_number=int(input("Please enter first number :-"))
second_number=int(input("Please enter second number :-"))


if first_number > second_number :
    print("{} is greater then {}".format(first_number,second_number))
elif second_number > first_number :
    print("{} is greate than {}".format (second_number,first_number))
else:
    print("BOTH NUMBERS ARE SAME")