year=int(input("Please give an year:-"))

if (year%4==0) and (year%100 !=0 or year%400 ==0):
    print("LEAP YEAR")
else:
    print("Not a leap year")
