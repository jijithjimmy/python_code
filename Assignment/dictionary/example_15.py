my_dict = {'x':500, 'y':5874, 'z': 560}
number=[ ]

for v in my_dict.values():
    number.append(v)
number.sort()
print(number)
length=len(number)
print("Smallest number will be :- ",number[0])
print("Lagest will be :-", number[length-1])


