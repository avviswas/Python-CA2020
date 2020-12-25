# 1.Create a list of given structure and get the Access list as provided below:

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#i)
x[5][:4]+x[6:8] 
#ii)
x[::2]
#iii)
x[::-1]   
#iv)
x[5][5][0]
#v)
x[:0]

#2. Create a list of thousand numbers using range and xrange and see the difference between each other.
#Ans)Range creates a list and stores it in the memory while xrange only creates a memory space when a particular index is called.

#3Tuples are immutable so they can be used to store sensitive data that cannot be changed while a list is mutable

