mydict = {5443:"Rahu", 7786: "Jimmy", 8762:"Manasha",6675:"Mukund", 9876:"Sheshadri"}

my_list=[ ]
for v in mydict.values():
    my_list.append(v)
my_list.sort()
print(my_list)


reverse_dictionary={ }

for k in mydict:
    val=mydict[k]
    reverse_dictionary[val]=k
print(reverse_dictionary)

result=[ ]

for item in my_list:
    tmp=[ ]
    tmp.append(item)
    tmp.append(reverse_dictionary[item])
    result.append(tmp)

print(dict(result))