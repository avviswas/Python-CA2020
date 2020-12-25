#5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in thestring with their index.

def rev_vow(a):
    string = []
    for i in a:
        if i in 'aeiouAEIOU':
            string.append(i)
    print(string[::-1])

