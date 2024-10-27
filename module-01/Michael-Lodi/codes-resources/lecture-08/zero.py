try:
    print(1/0)
except ZeroDivisionError:
    print('everything is fine')
print('ok!')

try:
    raise ZeroDivisionError
except IndexError:
    print('index')
print('lll')