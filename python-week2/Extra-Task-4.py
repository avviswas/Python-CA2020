#4.Write a program in Python to iterate through the list of numbers
# in the range of 1,100 and printthe number which is divisible by 3 and is a multiple of 2.

for i in range(0,100):
    if (i%3==0 and i%2==0):
        print(i)

