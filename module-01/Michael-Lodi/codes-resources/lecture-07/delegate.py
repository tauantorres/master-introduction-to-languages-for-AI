class E:
    def __init__(self,y):
        self.ee=y
    def g(self):
        return self.f()
class H(E):
    def f(self):
        return 100
