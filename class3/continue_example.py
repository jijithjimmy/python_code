starting_number=int(input("Please enter the starting limit :-"))
ending_number=int(input("Please enter the ending limit :-"))

for counter in range(starting_number,ending_number+1):
    if counter%5 == 0:
        continue
    print(counter)