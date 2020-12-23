string = input('Enter a combination of letters and strings: ')

digits = 0
letters = 0

for i in string:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
    else:
        pass

print('Letters ',letters,"Digits ",digits)