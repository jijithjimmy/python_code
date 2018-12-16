fruits = { "orange" : "A sweet and sour fruit",
           "apple": "good for health",
           "leamon": "has vitanin C in it ",
           "carrot": "Used as a salad",
           "mango": "Best summer fruit"}

fruits_list=[ ]

for keys in fruits.keys():
    fruits_list.append(keys)
fruits_list.sort()

for final_keys in fruits_list:
    print("{}:{}".format(final_keys,fruits[final_keys]))