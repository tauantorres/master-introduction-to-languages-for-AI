class NoIaddEx:
    def __init__(self,val):
        self.x=val
    def __add__(self,other):
        return NoIaddEx(self.x+other.x)
#     def __iadd__(self,other):
#         self.x=self.x+other.x
#         return self

S=NoIaddEx(10)
T=NoIaddEx(20)
print(id(S))  #some identity
S+=T
print(S.x)  # 30
print(id(S))  # new identity


class AugmentedEx:
    def __init__(self,val):
        self.x=val
    def __add__(self,other):
        return AugmentedEx(self.x+other.x)
    def __iadd__(self,other):
        self.x=self.x+other.x
        return self

S=AugmentedEx(10)
T=AugmentedEx(20)
print(id(S))  #some identity
S+=T
print(S.x)  # 30
print(id(S))  #same identity