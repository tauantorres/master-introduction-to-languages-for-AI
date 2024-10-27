try:
    print(1/0)
except IndexError:
    print('ok!')
print('after')
