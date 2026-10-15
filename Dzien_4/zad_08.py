from abc import ABC, abstractmethod

class Pojazdy(ABC):
    def __init__(self):
        self.predkosc=0
    @abstractmethod
    def przyspiesz(self):
        pass
    @abstractmethod
    def zwolnij(self):
        pass

class Sportowe(Pojazdy):
    def __init__(self):
        super().__init__()
    def przyspiesz(self):
        self.predkosc+=10
    def zwolnij(self):
        self.predkosc-=10

bmw=Sportowe()
bmw.przyspiesz()
print(bmw.predkosc)