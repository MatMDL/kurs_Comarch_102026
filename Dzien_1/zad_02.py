# imie = "Robert"
# wiek = 100

# print("Jestem " + imie + " mam " + str(wiek) + " lat")

# suma = 10
# roznica = 40
# srednia = 54.54

# print(f"Suma: {suma}, roznica: {roznica}, srednia: {srednia}")
# print(f"Jestem {imie} mam {wiek} lat")

# # imie = input("Podaj swoje imie: ")
# # wiek = input("Podaj swoj wiek: ")

# # print(type(imie), type(wiek))

# a = int(input("Podaj liczbe a: "))
# b = int(input("Podaj liczbe b: "))

# suma=a+b
# print(suma)

pWoda = 2.35
pSok = 2.00
pCola = 47.65

while True:
    try:
        cWoda = int(input("Podaj ilość wody: "))
        cSok = int(input("Podaj ilość soku: "))
        cCola = int(input("Podaj ilość coli: "))
        break
    except:
        print("Podaj liczbe\n")

suma=(pWoda*cWoda)+(pSok*cSok)+(pCola*cCola)
print(f"Suma: {suma}")