a = input('Enter an alpha numeric string: ')

list = []

for i in a:
    if i.isalpha():
        if i not in list:
            list.append(i)
            #print(list)
for j in list:
    print(j,' = ',a.count(j))