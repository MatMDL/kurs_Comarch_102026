# ############# lista

# ### tworzy
# # puste
# dane = []
# # zapelnione
# dane2 = [11, 4.5, "HELLO",11,44,11,66,11]

# ### odczytuje
# # print(dane2)
# # print(dane2[0])
# # print(dane2[1])
# # print(dane2[2])
# # print(dane2[-1]) # *

# ### dodaje
# # print(dane)
# # dane.append(2) # na koniec listy
# # dane.append(5)
# # dane.append("TEST")
# # print(dane)
# # dane.insert(1, 100) # w dowolne miejsce w liscie
# # print(dane)

# ### usuwa
# # print(dane2)
# # po indeksie
# # print(dane2)
# # dane2.pop(3)
# # print(dane2)

# # po wartosci
# # print(dane2)
# # dane2.remove(11)
# # print(dane2)

# ### edytuje
# # print(dane2)
# # dane2[0] = "???"
# # print(dane2)

# ### sprawdza czy istnieje wartosc w liscie
# # print(dane2)
# # print(44 in dane2)
# # print(dane2.index(11)) # zwraca indeks wystapienia pierwszej wartosci

# ### dlugosc listy
# # print(len(dane), len(dane2), dane2)

# print(bool(1), bool(0))
# print(bool("abc"), bool(""))

# a = [11,22,33]
# print(type(a))
# print(a)
# print(a[0])

# b = a
# a[1] = 100
# print(a, b)

# a = [11,22,33]
# b = a.copy()
# a[1] = 100
# print(a, b)

# dane=[]
# print(dane)
# dane.append(2)
# dane.append(5)
# print(dane)
# dane.insert(0,5)    # index, wartość
# print(dane)

# dane.pop(0) # usun po indexie
# dane.remove(2) # usun po wartosci
# print(dane)

# dane.append(5)
# dane.append(5)
# dane.append(5)
# dane.remove(5)
# print(dane)

# print(2 in dane)

# for _ in range(0,5):
#     dane.append(5)

# print(len(dane))

# while(5 in dane):
#     dane.remove(5)
#     print(dane)

imienia = []
for i in range(0,5):
    imienia.append(input(f"Podaj imie {i+1}: "))

for i in imienia:
    print(f"Testowe imie {i} to {imienia.index(i)} imie z listy")


a = "A"
b = "B"

a,b = b,a
print(a,b)

# ############ krotka

# ### tworzy
# # puste
# dane = () # NIE MA SENSU !
# # zapelnione
# dane2 = (11, 22, 5.5, "HELLO") # PEP8

# ### odczytuje
# # print(dane2)
# # print(dane2[0])
# # print(dane2[1])
# # print(dane2[-1])

# ### dodaje
# # NIE MA

# ### usuwa
# # NIE MA

# ### edytuje
# # NIE MA

# ### sprawdza czy istnieje wartosc w krotce
# # print(22 in dane2)
# # print(dane2)

# ### dlugosc krotki
# # print(len(dane2))############ krotka

# ### tworzy
# # puste
# dane = () # NIE MA SENSU !
# # zapelnione
# dane2 = (11, 22, 5.5, "HELLO") # PEP8

# ### odczytuje
# # print(dane2)
# # print(dane2[0])
# # print(dane2[1])
# # print(dane2[-1])

# ### dodaje
# # NIE MA

# ### usuwa
# # NIE MA

# ### edytuje
# # NIE MA

# ### sprawdza czy istnieje wartosc w krotce
# # print(22 in dane2)
# # print(dane2)

# ### dlugosc krotki
# # print(len(dane2))

############# zbiory

# ### tworzy
# # puste
# dane = set()
# # zapelnione
# dane2 = {1,4,7,"HELLO",4.3,4,4,4,4,4,8, "HELLO"}

# ### odczytuje
# # print(dane2)

# ### dodaje
# # print(dane)
# # dane.add(4)
# # dane.add(41)
# # dane.add(3)
# # dane.add(38)
# # print(dane)
# # dane.add(3)
# # dane.add(3)
# # dane.add(3)
# # dane.add(300)
# # print(dane)

# ### usuwa
# # print(dane2)
# # dane2.remove(4)
# # print(dane2)

# ### edytuje
# # NIE MA

# ### sprawdza czy istnieje wartosc w zbiorze
# # print(10 in dane2, dane2)

# ### dlugosc zbioru
# print(len(dane2))