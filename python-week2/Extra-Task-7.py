#7.Write a program in python to print the pair of numbers whose sum is equal to the resultnumber that is let's say 8.

for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if (x[i] + x[j] == 8):
            print('(',x[i],',',x[j],')')

