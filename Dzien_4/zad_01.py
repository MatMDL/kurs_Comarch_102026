class Student:
    def __init__(self,imie,nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
        self.oceny=[]
    def dodajOcene(self,ocena):
        self.oceny.append(ocena)
    def wypiszOceny(self):
        for o in self.oceny:
            print(f"Ocena: {o}")
    def policzSrednia(self)->float:
        suma=0
        for o in self.oceny:
            suma+=o
        if len(self.oceny)>0:
            return (suma/len(self.oceny))
        else:
            return 0

listaStudentow = []

while True:
    
    menu = int(input("1-dodaj studenta, 2-pokaz studentow, 3-usun studenta,"
                     "4-dodaj ocene studentowi, 5-wyswietl oceny studenta, "
                     "6-wyswietl srednia studenta, 7-koniec"))
    
    if menu == 1:
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        listaStudentow.append(Student(imie,nazwisko))
    elif menu == 2:
        for s in listaStudentow:
            print(f"Imie: {s.imie} Nazwisko: {s.nazwisko}")  
    elif menu == 3:
        nazwisko = input("Podaj nazwisko: ")
        for s in listaStudentow:
            if s.nazwisko==nazwisko:
                listaStudentow.remove(s)
                break
    elif menu == 4:
        nazwisko = input("Podaj nazwisko: ")
        ocena = int(input("Podaj ocene: "))
        for s in listaStudentow:
            if s.nazwisko==nazwisko:
                s.dodajOcene(ocena)
                break
    elif menu == 5:
        nazwisko = input("Podaj nazwisko: ")
        for s in listaStudentow:
            if s.nazwisko==nazwisko:
                s.wypiszOceny()
                break
    elif menu == 6:
        nazwisko = input("Podaj nazwisko: ")
        for s in listaStudentow:
            if s.nazwisko==nazwisko:
                print(s.policzSrednia())
                break    
    elif menu == 7:
        break