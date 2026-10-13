# # for i in range(0,5,1):
# #     print(i)

# # for i in range(0,5):
# #     # liczba = int(input(f"Podaj liczbe {i}:"))
# #     print(i)

# # for i in range(5):
# #     liczba = int(input(f"Podaj liczbe {i}:"))

# ########################################################

# ##### listy
# # dane = ["Kamil","Mateusz","Janusz" ]
# # for i in range(len(dane)):
# #     print(i, dane[i])

# # for x in dane: # foreach
# #     print(x)

# # for i,x in enumerate(dane): # foreach, tam gdzie wystepuja indexy
# #     print(i,x)

# ##### krotki
# # dane = (11,22,33,44,55)
# # for i in range(len(dane)):
# #     print(i, dane[i])

# # for x in dane: # foreach
# #     print(x)

# # for i,x in enumerate(dane): # foreach, tam gdzie wystepuja indexy
# #     print(i,x)

# ##### zbiory
# # dane = {11,22,33,44,55}

# # for x in dane: # foreach
# #     print(x)


# ##### slowniki
# # dane = {"sok":11,"woda":22,"cola":33}

# # for x in dane: # foreach, na paramter x zwracay jest klucz
# #     print(x, dane[x], dane.get(x))
# dane = []
# for i in range(1, 11):
#     dane.append(i)

# print(dane)

# ##################################################

# dane2 = {i:i**2 for i in range(1, 11)}
# print(dane2)

# dane3 = [i for i in range(1, 11) if i % 2 == 0]
# print(dane3)

if False:
    dane = []
    for i in range(10,0,-1):
        dane.append(i)
    print(dane)

    dane2=[i for i in range(10,0,-1)]
    print(dane2)

    dane3 = [i for i in range(10,0,-1) if i%2==0]
    print(dane3)

    dane4 = {i:i**2 for i in range(10,0,-1)}
    print(dane4)




nums=[]
for i in range(5):
    nums.append(int(input(f"Podaj liczbe {i+1}: ")))

print(nums)
print(f"Suma: {sum([i for i in nums if i%2==0])}")

nieParz=[i for i in nums if i%2!=0]
if len(nieParz)>0:
    iloczyn=1
    for i in nieParz:
        iloczyn*=i
else:
    iloczyn=0

print(f"Iloczyn: {iloczyn}")
