zbior = set()
# zbior.add(int(input("Podaj liczbe: ")))
# zbior.add(int(input("Podaj liczbe: ")))
# zbior.add(int(input("Podaj liczbe: ")))
# zbior.add(int(input("Podaj liczbe: ")))
# zbior.add(int(input("Podaj liczbe: ")))

print(f"Jest {len(zbior)} liczb")

dane={}
dane2={"Woda":1.11,"Sok":2.22,"Cola":3.33}
print(dane2.get("Woda"),dane2["Woda"])

dane2["Kiwi"]=4.44
print(dane2)

print("Sok" in dane2)
print("Sok" in dane2.keys())
print(2.22 in dane2.values())

# ############# słownik

# ### tworzy
# # puste
# dane = {}
# # zapelnione
# dane2 = {"woda":1.11, "sok":2.22, 100:"sto", 5:125, "Hello":":)"}
# # print(dane2)

# ### odczytuje
# # print(dane2)
# # print(dane2["woda"])
# # print(dane2["sok"], dane2.get("sok"))
# # print(dane2[100], dane2.get(100))
# # print(dane2[5], dane2.get(5))

# ### dodaje
# # print(dane2)
# # dane2["kiwi"] = 4.44
# # print(dane2)
# # dane2["sok"] = 9.99
# # print(dane2)

# ### usuwa
# # print(dane2)
# # dane2.pop("sok")
# # dane2.pop(5)
# # print(dane2)

# ### edytuje
# # dane2["sok"] = 9.99 # warunek: klucz juz musi istniec

# ### sprawdza czy istnieje KLUCZ w slowniku
# print(dane2)
# print("sok" in dane2)
# print("sok" in dane2.keys())

# print(2.22 in dane2.values())


# ### dlugosc slownika
# print(len(dane2))