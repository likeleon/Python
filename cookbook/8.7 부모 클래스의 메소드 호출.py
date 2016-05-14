#
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

b = B()
b.spam()


#
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C.__init__')

c = C()
print(C.__mro__)


#
class A:
    def spam(self):
        print('A.spam')
        super().spam()

class B:
    def spam(self):
        print('B.spam')

class C(A, B):
    pass

c = C()
c.spam()