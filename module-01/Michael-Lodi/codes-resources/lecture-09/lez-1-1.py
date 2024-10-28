import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b
print('a: ', a)
print('b: ', b)
print('c=a+b: ', c)

d=np.array([10])
print('d: ', d)
e=d+a
print('e=d+a: ', e)

f=10+a
print('f=10+a: ', f)

def foo(x,y):
    return x+y

# vectorisation and broadcasting apply also to
# simple user defined functions

print('foo(a,b): ', foo(a,b))

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[1,1,1],[3,3,3]])
print('x: ',x)
print('y: ',y)
print('foo(x,y): ', foo(x,y))