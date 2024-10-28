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


t=np.arange(12).reshape(2,2,3)
print(t)

v=np.arange(10).reshape(2,5)
print('v: ', v)
print('np.sum(v): ', np.sum(v))
print('np.sum(v, axis=0): ', np.sum(v, axis=0))
print('np.sum(v, axis=1): ', np.sum(v, axis=1))

Ones = np.array([[1,1,1],[1,1,1]])
Twos = np.array([[2,2,2],[2,2,2]])

Conc_over0 = np.concatenate([Ones, Twos], axis = 0)
print('Conc_over0: ', Conc_over0)
Conc_over1 = np.concatenate([Ones, Twos], axis = 1)
print('Conc_over1: ', Conc_over1)


t=np.arange(12).reshape(2,2,3)
print('t: ')
print(t)
print('np.sum(t, axis=0): ')
print(np.sum(t, axis=0))
print('np.sum(t, axis=1): ')
print(np.sum(t, axis=1))
print('np.sum(t, axis=2): ')
print(np.sum(t, axis=2))
