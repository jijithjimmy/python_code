shopping_list=[ ]

keep_going='y'

while keep_going == 'y':
    name_of_product=input("Please enter a prdct name :- ")
    shopping_list.append(name_of_product)
    #print()
    #print()

    keep_going=input("Please enter 'y' if you need to continue :-")

print("The filled lists is :-", shopping_list)
print(shopping_list[0]

##sort and sorted difference
##shopping_list.sort()
##sorted_shopping_list=sorted(shopping_list)   >> creating a new space in memmory without touching the original list .
## doing changes there and giving you an input
