class A:
    def f(self):
        return 'f in A'
class B:
    def f(self):
        return 'g in B'
class C(A,B):
    def h(self):
        return 'h in C'
    def m(self):
        return super().g()
        