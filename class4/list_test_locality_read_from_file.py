myfile=open('place_list.txt','r')
file_content=myfile.readlines()
#print(file_content)

places=[ ]

for counter in  range(len(file_content)):
    print(file_content[counter])