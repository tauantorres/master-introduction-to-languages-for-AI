'''example of how "private" names are istead
just mangled by the Python interpreter
'''

class A:
    def __init__(self):
        self.__S=0

a=A()
# print(a.__S) #this is an error

#not really private--just name mangling
print(a._A__S)