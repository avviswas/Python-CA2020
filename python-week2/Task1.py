# 1. Create three variables in a single line and assign values to them in such a manner that each one ofthem belongs to a different data type.
a, b, c = 2, 2.03, 'string'

# 2.Create a variable of type complex and swap it with another variable of type integer.
a = complex(1,2)
b = 2
a = b
print(type(a))

# 3.Swap two numbers using a third variable and do the same task without using any third variable.

#with third variable
a,b = 1,2
c = a
a = b
b = c
print(a,b)

#without third variable
a,b = 1,2
a,b = b,c
print(a,b)

# 4.Write a program that takes input from the user and prints it using both Python 2.x and Python 3.xVersion.

# Python 2.x 
a = raw_input('Input a value: ')

#Python 3.x
a = input('input a value: ')

# 5.Write a program to complete the task given below:Ask users to enter any 2 numbers in between 1-10 , 
# add the two numbers and keep the sum inanother variable called z. Add 30 to z and store the output in variable result 
# and print result as thefinal output.

a = int(input('enter a value between 1 and 10: '))
b = int(input('enter another value between 1 and 10: '))
z = a+b
result = 30 + z
print('Final Result: ', result)

# 6.Write a program to check the data type of the entered values.

a = eval(input('enter any value : '))
print("The data type of the input value is ",type(a))

# 7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

CamelCase = 1
CAMELCASE = 2
Camel_Case = 3
camelcase = 4
CAMELCASE = 5

# string = CamelCase
# string.lower()
# string.upper()
# string.capitalize()

# 8.If one data type value is assigned to ‘a’ variable and then a different 
# data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?
#Answer:Yes, in python the latest declaration is considered as the value of the variable

