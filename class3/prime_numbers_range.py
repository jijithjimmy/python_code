start=int(input("Please enter a starting range of number :- "))
end=int(input("Please enter the end limit :- "))


if start > 1:
    for isPrime in range(start,end):
        for counter in range(2,isPrime):
            if isPrime % counter == 0:
                #print("Not a prime number !!!")
                break

        else:
            print(isPrime ,"is a Prime number ")

else:
    print("Not a prime number !!!")