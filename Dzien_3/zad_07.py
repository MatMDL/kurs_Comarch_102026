class Kurs:
    def __init__(self, nazwa, termin):
        self.nazwa=nazwa
        self.termin=termin
        self.lista=[]
    def dodaj(self, k):
        self.lista.append(k)
    def usun(self, k):
        self.lista.append(k)
    def drukujInformacje(self):
        print(f"Kurs: {self.nazwa}, {self.termin}, Lista osob:")
        for x in self.lista:
            print(x)

class Kursant:
    def __init__(self, imie, nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
    def __str__(self):
        return (f"{self.imie} {self.nazwisko}")

listaKursow=[]

while True:

    menu = int(input("1-dodaj kurs, 2-pokaz kursy, 3-usun kurs, 4-dodaj kursanta do kursu, 5-wyswietl kurs wraz z kursantami, 6-usun kursanta z kursu, 7-koniec"))

    if menu == 1:
        nazwa = input("Podaj nazwe kursu:")
        termin = input("Podaj termin kursu:")
        listaKursow.append(Kurs(nazwa,termin))
    elif menu == 2:
        for x in listaKursow:
            print(f"Nazwa: {x.nazwa} Termin: {x.termin}")

    elif menu == 3:
        nazwa = input("Podaj nazwe kursu:")
        for x in listaKursow:
            if x.nazwa == nazwa and not len(x.lista)>0:
                listaKursow.remove(x)
                break

    elif menu == 4:
        nazwa = input("Podaj nazwe kursu:")
        imie = input("Podaj imie kursanta:")
        nazwisko = input("Podaj nazwisko kursanta:")
        for x in listaKursow:
            if x.nazwa == nazwa:
                x.lista.append(Kursant(imie,nazwisko))
                break

    elif menu == 5:
        nazwa = input("Podaj nazwe kursu:")
        for x in listaKursow:
            if x.nazwa == nazwa:
                x.drukujInformacje()

    elif menu == 6:
        nazwa = input("Podaj nazwe kursu:")
        nazwisko = input("Podaj nazwisko kursanta:")
        for x in listaKursow:
            if x.nazwa == nazwa:
                for y in x.lista:
                    if y.nazwisko==nazwisko:
                        x.lista.remove(y)
                        break
        
    elif menu == 7:
        break