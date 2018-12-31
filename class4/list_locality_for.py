infile=open('place_list.txt','r')
file_content=infile.readlines()

#print(file_content)
correct_list=[ ]

for counter in range(len(file_content)):
    tmp=(file_content[counter].rstrip('\n'))
    #tmp=tmp.rstrip('\n')
    correct_list.append(tmp)

input_place=input("Please enter a place name :- ")

if input_place.lower() in correct_list:
    print("Delivery is available !!!")
else:
    print("No delivery !!! sorry !!!")