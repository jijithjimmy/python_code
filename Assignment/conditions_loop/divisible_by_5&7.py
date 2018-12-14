divisible_by_7=[ ]
divisible_by_7_multiple_by_5=[ ]

for counters in range(1500,2701):
    if (counters % 7 ) == 0:
        divisible_by_7.append(counters)


for counter in divisible_by_7:
    if counter % 5 == 0:
        divisible_by_7_multiple_by_5.append(counter)

print(divisible_by_7_multiple_by_5)

