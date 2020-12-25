#6.Write a program in Python to iterate through the string “hello my name is abcde” and print the string which is having an even length.

x = 'hello my name is alvin'
y = x.split()
even_list = []
for i in y:
    if len(i) % 2 == 0:
        even_list.append(i)
print (even_list)

