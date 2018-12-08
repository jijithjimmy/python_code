number=int(input("Please enter a number :-  "))

if number > 1 :
    for counter in range (2,number):
        if number % counter == 0:
            print(number, ":- is not a prime number!!!")
            break
    else:
        print(number, ":- is a prime number!!!")

else:
    print("NOT A PRIME NUMBER !!! Its a default rule")