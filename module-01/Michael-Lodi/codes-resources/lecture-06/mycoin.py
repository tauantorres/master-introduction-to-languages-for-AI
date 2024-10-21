# 0 stands for head
# 1 stands for tail
from random import randint

class Coin:
    def __init__(self):
        self.__c=0
    def toss(self):
        self.__c=randint(0,1)
    def show(self):
        return self.__c


    