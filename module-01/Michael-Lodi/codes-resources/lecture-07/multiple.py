class A:
    def f(self):
        return 10
class B:
    def f(self):
        return 100
class C(A,B):
    pass

c=C()
print(c.f())  # 10  //  look at the order of A,B in the def of C

class D(B,A):
    pass
d=D()
print(d.f())  # 100