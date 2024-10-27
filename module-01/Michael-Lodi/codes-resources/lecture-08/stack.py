def f():
    a=0
    return g()
def g():
    b=0
    return h()
def h():
    c=0
    return 1/0  #ZeroDivisionError raised
try:
    print(f())
except ZeroDivisionError:
    print('Excpname caught')