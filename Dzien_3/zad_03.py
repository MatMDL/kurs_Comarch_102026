from pathlib import Path
kt = Path(__file__).parent / "kt.txt"

def dodaj(i,n,t,e):
    global kt
    with open(kt,"a",encoding="utf8") as f: 
        f.write(f"{i};{n};{t};{e}\n")

def pokaz():
    global kt
    with open(kt,"r",encoding="utf8") as f:
        for l in f:
            print(l)

def usun(n):
    global kt
    dane=[]
    with open(kt,"r",encoding="utf8") as f:
        dane=f.readlines()
    for x in dane:
        linie = x.strip().split(";")
        if linie[1]==n:
            dane.remove(x)
            break
    with open(kt,"w",encoding="utf8") as f:
        f.writelines(dane)

def zmien(i,n,t,e):
    global kt
    dane=[]
    nowe=f"{i};{n};{t};{e}\n"
    with open(kt,"r",encoding="utf8") as f:
        dane=f.readlines()
    for x in dane:
        linie = x.strip().split(";")
        if linie[1]==n:
            dane[dane.index(x)]=nowe
            break
    with open(kt,"w",encoding="utf8") as f:
        for l in dane:
            f.write(l)


while True:
    menu=int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec"))
    if menu==1:
        imie=input("Podaj imie: ")
        nazwisko=input("Podaj nazwisko: ")
        telefon=input("Podaj telefon: ")
        email=input("Podaj email: ")
        dodaj(imie,nazwisko,telefon,email)
    elif menu==2:
        pokaz()
    elif menu==3:
        nazwisko=input("Podaj nazwisko: ")
        usun(nazwisko)
    elif menu==4:
        imie=input("Podaj imie: ")
        nazwisko=input("Podaj nazwisko: ")
        telefon=input("Podaj telefon: ")
        email=input("Podaj email: ")
        zmien(imie,nazwisko,telefon,email)
    elif menu==5:
        break