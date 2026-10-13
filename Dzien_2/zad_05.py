sklep = {"chleb":1.11,"sok":2.22,"woda":3.33}
koszyk = []

while True:
    menu = int(input("1-dodaj produkt, 2-pokaz koszyk, 3-usun produkt, 4-kasa/koniec\n"))

    if menu == 1:
        produkt = input("Podaj nazwe produktu do dodania: ")
        if produkt in sklep:
            koszyk.append(produkt)
        else:
            print(f"Brak produktu {produkt}")
    if menu == 2:
        print("Produkt: ")
        for i in range(len(koszyk)):
            print(f"{i+1}: {koszyk[i]}")
    if menu == 3:
        produkt = input("Podaj nazwe produktu do usuniecia: ")
        if produkt in koszyk:
            koszyk = [x for x in koszyk if x != produkt]
        else:
            print("Brak produktu w koszyku")
    if menu == 4:
        print("Paragon:")
        suma=0
        for produkt in sklep:
            print(f"Produkt: {produkt}, ilość {koszyk.count(produkt)}, cena: {koszyk.count(produkt) * sklep[produkt]}")
            suma+=koszyk.count(produkt) * sklep[produkt]
        print(f"Do zapłaty: {suma}")
        break