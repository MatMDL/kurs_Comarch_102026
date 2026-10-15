class Pracownik:
    def __init__(self,imie,nazwisko,wynagrodzenie):
        self.__imie=imie
        self.__nazwisko=nazwisko
        self.__wynagrodzenie=wynagrodzenie
    def getImie(self):
        return self.__imie
    def getNazwisko(self):
        return self.__nazwisko
    def getWynagrodzenie(self):
        return self.__wynagrodzenie
    def setImie(self,imie):
        self.__imie=imie
    def setNazwisko(self,nazwisko):
        self.__nazwisko=nazwisko
    def setWynagrodzenie(self,wynagrodzenie):
        self.__wynagrodzenie=wynagrodzenie

listaPracownkow = []

while True:
    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmiana wynagrodzenia, "
                     "5-zmiana danych pracownika, 6-koniec"))

    if menu == 1:
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        wynagrodzenie = int(input("Podaj wynagrodzenie: "))
        listaPracownkow.append(Pracownik(imie,nazwisko,wynagrodzenie))
    elif menu == 2:
        for p in listaPracownkow:
            print(f"Imie: {p.getImie()} Nazwisko: {p.getNazwisko()}  Wynagrodzenie: {p.getWynagrodzenie()} ")
    elif menu == 3:
        nazwisko = input("Podaj nazwisko: ")
        for p in listaPracownkow:
            if p.getNazwisko()==nazwisko:
                listaPracownkow.remove(p)
                break
    elif menu == 4:
        nazwisko = input("Podaj nazwisko: ")
        noweWynagrodzenie = int(input("Podaj nowe wynagrodzenie: "))
        for p in listaPracownkow:
            if p.getNazwisko()==nazwisko:
                p.setWynagrodzenie(noweWynagrodzenie)
                break
    elif menu == 5:
        nazwisko = input("Podaj nazwisko: ")
        noweImie = input("Podaj nowe imie: ")
        noweNazwisko = input("Podaj nowe nazwisko: ")
        for p in listaPracownkow:
            if p.getNazwisko()==nazwisko:
                p.setImie(noweImie)
                p.setNazwisko(noweNazwisko)
                break 
    elif menu == 6:
        break