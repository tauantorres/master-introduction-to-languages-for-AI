n=input('give me a number or stop: ')
while n != 'stop':
    try:
        print(int(n)**2)
    except ValueError:
        print('bad!')
    n=input('give me a number or stop: ')
print('Bye')
