import random

keep_going='y'

while keep_going.lower() == 'y':

    random_number = random.randint(1,9)
    user_input = int(input("Please enter a number between 1 and 9 :- "))

    if user_input == random_number:
        print("Congrats !!! You guessed the correct number")
        break
    else:
        print("Please try again since your guess is wrong!!!")
        print()
        keep_going=input("Please enter y to continue :-")


