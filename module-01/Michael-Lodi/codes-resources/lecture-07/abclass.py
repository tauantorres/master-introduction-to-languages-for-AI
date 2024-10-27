from abc import ABC,abstractmethod

class E(ABC):
    def __init__(self,y):
        self.ee=y
    @abstractmethod
    def f(self):
        pass
    def g(self):
        return self.f()
class H(E):
    def f(self):
        return 100

# e=E(10)
      # error: Can't instantiate abstract class E
                # with abstract methods f
# print(e.g())
h=H(20)
print(h.g())
