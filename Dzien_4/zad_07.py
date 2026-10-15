class A:
    def __init__(self,a):
        print("A")
        self.poleA=a

class B:
    def __init__(self,b):
        print("B")
        self.poleB=b

class C(A,B):
    def __init__(self,a,b,c):
        print("C")
        A.__init__(self,a)
        B.__init__(self,b)
        self.poleC=c

ob=C('a','b','c')
print(ob.poleA,ob.poleB,ob.poleC)