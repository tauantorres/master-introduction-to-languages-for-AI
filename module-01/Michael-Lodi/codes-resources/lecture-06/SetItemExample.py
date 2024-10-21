class SetItEx:
    def __init__(self):
        self.V=[1]
        self.ll=0
    def __len__(self):
        return len(self.V)+self.ll
    def __getitem__(self,key):
        return self.V[key]
    def __setitem__(self, key, val):
        if key>len(self.V):
            return None
        if key==len(self.V):
            self.V.append(val)
        else:
            self.V[key]=val

# S=SetItEx()
# print(len(S))  # 0  Calls __len__
# S[0]=10
# print(len(S))  # 1  Calls __setitem__
# print(S[0])    # 10 Calls __getitem__