from random import randint
class Coin:
    def __init__(self):
        self.__c=randint(0,1)  #private
    def show(self):
        return self.__c
    def toss(self):
        self.__c=randint(0,1)
    def setc(self,value):
        if value == 0 or value ==1:
            self.__c=value
