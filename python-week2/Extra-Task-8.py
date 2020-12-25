#8.

even_list = []
odd_list = []

while (len(even_list) < 5) or (len(odd_list) < 5):
    num = int(input('Enter number: '))
    if num > 1 and num < 51:
        if (num%2 == 0 ):
            even_list.append(num)
        else:
            odd_list.append(num)
    else:
        num = int(input('Enter number between 1 and 50: '))
else:
    print('sum of even_list is',sum(even_list[:5]),'sum of odd_list is',sum(odd_list[:5]))