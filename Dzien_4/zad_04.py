class Pojazdy():
    def __init__(self):
        self.nazwa=None
        self.kolor=None
        self.waga=None
    def odpalSilnik(self):
        print("wrrrrr")

class Samolot(Pojazdy):
    def __init__(self):
        self.pulap = None
    def lec(self):
        print("lece")

class Lodz(Pojazdy):
    def __init__(self):
        self.wypornosc = None
    def plyn(self):
        print("plyne")

samolot = Samolot()
lodz = Lodz()
# ************************************************************************
class A:
    def __init__(self):
        self.polA=None
    def MetodaA(self):
        print("A")
class B(A):
    def __init__(self):
        self.polB=None
    def MetodaB(self):
        print("B")
class C(B):
    def __init__(self):
        self.polC=None
    def MetodaC(self):
        print("C")

obC = C()
obC.MetodaA()
# ************************************************************************
class AA:
    def __init__(self):
        self.polA=None
    def MetodaAA(self):
        print("AA")
class BB():
    def __init__(self):
        self.polB=None
    def MetodaBB(self):
        print("BB")
class CC(AA,BB):
    def __init__(self):
        self.polC=None
    def MetodaCC(self):
        print("C")
    def MetodaBB(self):
        super().MetodaBB()
        print("BB w C")

obCC = CC()
obCC.MetodaAA()
obCC.MetodaBB()
# ************************************************************************
class Poj:
    def __init__(self,nazwa,kolor):
        self.nazwa=nazwa
        self.kolor=kolor

class Sam(Poj):
    def __init__(self, nazwa, kolor,pulap):
        super().__init__(nazwa, kolor)
        self.pulap=pulap

sam=Sam("F15","GR",22)
print(sam.nazwa, sam.kolor, sam.pulap)
# ************************************************************************
