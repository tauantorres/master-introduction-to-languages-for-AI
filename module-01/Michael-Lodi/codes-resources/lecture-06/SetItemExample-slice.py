class SetItEx:
    def __init__(self):
        self.V=[10,20,30,40]
    def __len__(self):
        return len(self.V)
    def __getitem__(self,key):
        if isinstance(key, slice):
            # we have a slice:
            return self.V[key.start:key.stop:key.step]
        else:
            # we have a plain index
            return self.V[key]
    def __setitem__(self, key, val):
        if key>len(self.V):
            return None
        if key==len(self.V):
            self.V.append(val)
        else:
            self.V[key]=val

S=SetItEx()
print(len(S))  # 4  Calls __len__
S[0]=10
print(len(S))  # 4  Calls __setitem__
print(S[0])    # 10 Calls __getitem__