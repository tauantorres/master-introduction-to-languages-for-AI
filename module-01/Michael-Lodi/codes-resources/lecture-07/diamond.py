class Top:
    def f(self):
        return 1000
class A(Top):
    def f(self):
        return 10
class B(Top):
    pass
class C(A,B):
    pass

c=C()
print(c.f())  # 10  //  look at the order of A,B in the def of C

class D(B,A):
    pass
d=D()
print(d.f())  # 10
