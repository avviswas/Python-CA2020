# Write a program in Python to perform the following operator based task:

num1 = int(input('add a number: '))
num2 = int(input('add another number: '))
option = int(input('Choose and Arithmetic Operation between 1 and 5: '))

if (option == 1):
    a = num1 + num2
    print(a)
    if (a<0):
        print('NEGATIVE')

elif (option == 2):
    a = num1 - num2
    print(a)
    if (a<0):
        print('NEGATIVE')

elif (option == 3):
    a = num1 / num2
    print(a)
    if (a<0):
        print('NEGATIVE')

elif (option == 4):
    a = num1 * num2
    print(a)
    if (a<0):
        print('NEGATIVE')

elif (option == 5):
    first = int(input('add another number: '))
    second = int(input('add another number: '))
    a = (num1 + num2 +first +second) / 4
    print(a)
    if (a<0):
        print('NEGATIVE')
    


