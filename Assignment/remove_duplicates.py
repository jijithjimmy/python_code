my_list=['jijith','jijith','jitha','jenita']

my_dict={ }
my_final_list=[ ]

for items in my_list:
    my_dict[items]="Random Stuff"

for keys in my_dict.keys():
    my_final_list.append(keys)

print(my_final_list)