number = 7

answer = int(input('guess the lucky number '))

while answer == number:
    break
else:
    while answer != number:
        answer = input("Do you want to continue guessing ")
        if answer =='no' or answer =='7':
            break
        
