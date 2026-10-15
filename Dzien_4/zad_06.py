class Uczen:
    def __init__(self,imie,nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
    def __eq__(self, other):
        return self.imie == other.imie and self.nazwisko == other.nazwisko
    
class UczenController:
    def __init__(self):
        self.listaUczniow=[]
    def dodajUcznia(self,u):
        self.listaUczniow.append(u)
    def pokazUczniow(self):
        for u in self.listaUczniow:
            print(u)
    def usunUcznia(self,u):
        if u in self.listaUczniow:
            self.listaUczniow.remove(u)
    def edytujUcznia(self,u1,u2):
        for i,u in enumerate(self.listaUczniow):
            if u==u1:
                self.listaUczniow[i]=u2
                break

class Szkola(UczenController):
    def __init__(self, nazwaSzkoly):
        super().__init__()
        self.nazwaSzkoly=nazwaSzkoly
    def menu(self):
        while True:
            m=input("D-dodaj, P-pokaz, U-usun, Z-zmien, K-koniec")
            match m:
                case "D":
                    i=input("Imie: ")
                    n=input("Nazwisko: ")
                    self.dodajUcznia(Uczen(i,n))
                case "P":
                    self.pokazUczniow()
                case "U":
                    i=input("Imie: ")
                    n=input("Nazwisko: ")
                    self.usunUcznia(Uczen(i,n))
                case "Z":
                    i=input("Imie: ")
                    n=input("Nazwisko: ")
                    iN=input("Nowe imie: ")
                    nN=input("Nowe nazwisko: ")
                    self.edytujUcznia(Uczen(i,n),Uczen(iN,nN))
                case "K":
                    break

szkola=Szkola("Test")
szkola.menu()