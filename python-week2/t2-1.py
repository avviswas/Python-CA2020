# 1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as astring.

a = int(input('Enter any integer: '))

if (a%3 == 0 and a%5 == 0):
    print('Consultadd - Python Training')
elif (a%3 ==0):
    print ('Consultadd')
elif (a%5 == 0):
    print('Python Training')


