class D(list):
    def enum(self):
        for e in self:
            print(e)
    def __len__(self):
        '''We may override the standard len(),
so that for instances of W return len+10
'''
        return super().__len__() + 10
