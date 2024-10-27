import collections.abc
class MyIter(collections.abc.Iterator):
#class MyIter:  #we iterate on even int in an interval
    def __init__(self,start,stop):
        if start%2!=0:
            start+=1
        self.x=start
        self.stop=stop
    def __iter__(self):  # return the iterator
        return self
#     def __next__(self):  # return the "next" object
#         if self.x<self.stop:
#             curr=self.x
#             self.x+=2
#             return curr
#         else:
#             raise StopIteration
F=MyIter(1,6)
for i in F:
    print(i)     # 2, 4
for i in F:      # F is already exhausted
    print('here I am')  # never executed

# an equivalent genertor
def MyGen(start,stop):
    if start%2!=0:
        start+=1
    return (i for i in range(start,stop,2))

for k in MyGen(1,6):
    print(k)     # 2,4
