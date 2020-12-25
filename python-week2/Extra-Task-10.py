tup = (1,2,3,4,5,6,7,8,9,10)

list = []
for i in tup:
    if i%2 == 0:
        list.append(i)
print(tuple(list))