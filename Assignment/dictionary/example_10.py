my_dict = {'data1':100,'data2':-54,'data3':247}
number_list=[ ]
sum=0

for values in my_dict.values():
    number_list.append(values)

for counter in number_list:
    sum=sum+counter

print("Total Sum will be :- ",sum)