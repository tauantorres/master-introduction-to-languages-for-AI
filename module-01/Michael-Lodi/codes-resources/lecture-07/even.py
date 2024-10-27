class Even:
    def __init__(self,start, stop):
        if start%2!=0: #start is odd
            start+=1
        self.x=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.x<self.stop:
            curr=self.x
            self.x+=2
            return curr
        else:
            raise StopIteration
        