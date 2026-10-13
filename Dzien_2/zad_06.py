kt = []

while True:
    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec\n"))
    if menu == 1:
        imie=input("Podaj imie: ")
        nazwisko=input("Podaj nazwisko: ")
        telefon=input("Podaj numer: ")
        kt.append([imie,nazwisko,telefon])
        print("Dodano\n")
    if menu == 2:
        for i in kt:
            print(f"Imie {i[0]}, Nazwisko {i[1]}, telefon {i[2]}")
    if menu == 3:
        nazwisko=input("Podaj nazwisko: ")
        usunieto=False
        for i in kt:
            if i[1]==nazwisko:
                # kt.pop(kt.index(i))
                kt.remove(i)
                print(f"Usunieto {nazwisko}\n")
                usunieto=True
                break
        if not usunieto:
            print(f"Nie znaleziono {nazwisko}\n")
    if menu == 4:
        imie=input("Podaj imie: ")
        nazwisko=input("Podaj nazwisko: ")
        telefon=input("Podaj numer: ")
        zaktualizowano=False
        for i in kt:
            if i[1]==nazwisko:
                i[0]=imie
                i[1]=nazwisko
                i[2]=telefon
                zaktualizowano=True
                print("Zaktualizowano\n")
                break
        if not zaktualizowano:
            print(f"Nie znaleziono {nazwisko}\n")
    if menu == 5:
        break