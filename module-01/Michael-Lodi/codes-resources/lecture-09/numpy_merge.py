import numpy as np
        
def exchangecolumns(a):
    if a.shape[1]%2 != 0:
        return None
    b = a.copy()
    a[:,::2],a[:,1::2] = b[:,1::2],b[:,::2]
    return a
def exchangecolumns2(a):
    if a.shape[1]%2 != 0:
        return None
#    b = a.copy()
    a[:,::2],a[:,1::2] = a[:,1::2],a[:,::2]
    return a
print(exchangecolumns(np.arange(0,6).reshape(3,2)))
print(exchangecolumns2(np.arange(0,6).reshape(3,2)))

print(exchangecolumns(np.arange(0,20).reshape(5,4)))
print(exchangecolumns2(np.arange(0,20).reshape(5,4)))
#a = np.array([[1,2,3,4],[4,5,6,7]])