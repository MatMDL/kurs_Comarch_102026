# class Samolot:

#     def __init__(self, nazwa, kolor, pulap):
#         self.nazwa =nazwa
#         self.kolor =kolor
#         self.pulap =pulap

#     def __str__(self):
#         return (f"{self.nazwa}")


# ob1 = Samolot("Boeing","zielony",9999)
# print(ob1)

class Pracownik:
    def __init__(self, imie, nazwisko, telefon):
        self.imie=imie
        self.nazwisko=nazwisko
        self.telefon=telefon

listaPracownikow=[]

while True:

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec"))
    if menu == 1:
        imie = input("Podaj imie:")
        nazwisko = input("Podaj nazwisko:")
        telefon = input("Podaj telefon:")

        listaPracownikow.append(Pracownik(imie, nazwisko, telefon))

    elif menu == 2:

        for p in listaPracownikow:
            print(f"Imię: {p.imie} Nazwisko: {p.nazwisko} Telefon: {p.telefon}")
        
    elif menu == 3:
        nazwisko = input("Podaj nazwisko:")
        flaga=False
        for p in listaPracownikow:
            if p.nazwisko == nazwisko:
                listaPracownikow.remove(p)
                print("Pomyslnie usunieto")
                flaga=True
                break
        if not flaga:
            print("Nie znaleziono pracownika o podanym nazwisku")
        
    elif menu == 4:
        nazwisko = input("Podaj nazwisko:")
        noweImie = input("Podaj nowe imie:")
        noweNazwisko = input("Podaj nowe nazwisko:")
        nowyTelefon = input("Podaj nowy telefon:")
        flaga=False
        for p in listaPracownikow:
            if p.nazwisko == nazwisko:
                p.imie=noweImie
                p.nazwisko=noweNazwisko
                p.telefon=nowyTelefon
                print("Pomyslnie zaktualizowano")
                flaga=True
                break
        if not flaga:
            print("Nie znaleziono pracownika o podanym nazwisku")

    elif menu == 5:
        break
