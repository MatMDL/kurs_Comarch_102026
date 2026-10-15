from abc import ABC, abstractmethod

class Pojazd(ABC):
    def __init__(self,marka,model,rok):
        self.marka=marka
        self.model=model
        self.rok=rok
    def pokaz_info(self):
        print(f"{self.marka} {self.model} {self.rok}")
    @abstractmethod
    def oblicz_koszt(self,dni):
        pass

class Silnik(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def uruchom_silnik(self):
        pass
    @abstractmethod
    def zatrzymaj_silnik(self):
        pass

class Samochod(Pojazd,Silnik):
    def __init__(self, marka, model, rok):
        super().__init__(marka, model, rok)
    def oblicz_koszt(self,dni):
        return (150*dni)
    def uruchom_silnik(self):
        print(f"{self.marka} {self.model} uruchomiono silnik")
    def zatrzymaj_silnik(self):
        print(f"{self.marka} {self.model} zatrzymano silnik")

class Motocykl(Pojazd,Silnik):
    def __init__(self, marka, model, rok):
        super().__init__(marka, model, rok)
    def oblicz_koszt(self,dni):
        return (100*dni)
    def uruchom_silnik(self):
        print(f"{self.marka} {self.model} uruchomiono silnik")
    def zatrzymaj_silnik(self):
        print(f"{self.marka} {self.model} zatrzymano silnik")

class Rower(Pojazd):
    def __init__(self, marka, model, rok):
        super().__init__(marka, model, rok)
    def oblicz_koszt(self,dni):
        return (30*dni)

p=Samochod("Toyota","Corolla",2022)
m=Motocykl("Yamaha","MT-07",2021)
r=Rower("Kross","Hexagon",2023)

p.pokaz_info()
print(f"Koszt za 3 dni {p.oblicz_koszt(3)}")
p.uruchom_silnik()
p.zatrzymaj_silnik()
print("-"*20)
m.pokaz_info()
print(f"Koszt za 3 dni {m.oblicz_koszt(3)}")
m.uruchom_silnik()
m.zatrzymaj_silnik()
print("-"*20)
r.pokaz_info()
print(f"Koszt za 3 dni {r.oblicz_koszt(3)}")
print("-"*20)
