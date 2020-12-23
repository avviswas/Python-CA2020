counter = 0

while counter < 5:
    counter+=1
    answer = int(input('guess the lucky number '))
    if (answer == 7):
        print('Good guess!')
        break
    else:
        print('Try again!')
else:
    print('Game over!')
