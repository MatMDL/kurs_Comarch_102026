# # while True:
# # 
# #     while True:
# #         try:
# #             liczba1 = int(input("Podaj liczbe 1: "))
# #         except ValueError:
# #             print("Wprowadz poprawnie liczbe !")
# #         else:
# #             break
# # 
# #     while True:
# #         try:
# #             liczba2 = int(input("Podaj liczbe 2: "))
# #             break
# #         except ValueError:
# #             print("Wprowadz poprawnie liczbe !")
# # 
# #     try:
# #         wynik = liczba1 / liczba2
# #         print(wynik)
# #     except ZeroDivisionError:
# #         print("Nie dziel przez 0 !")



# while True:
#     try:
#         liczba1 = int(input("Podaj liczbe 1: "))
#         liczba2 = int(input("Podaj liczbe 2: "))
#         wynik = liczba1 / liczba2
#         # dane = [11,22]
#         # print(dane[100])
#         print(wynik)
#     except ZeroDivisionError:
#         print("Nie dziel przez 0 !")
#     except ValueError:
#         print("Wprowadz poprawnie liczbe !")
#     except Exception as e:
#         print(e)
#         print(type(e).__name__)
#         print("Wystapil blad !")
#     else:
#         print("TU BLOK ELSE")
#     finally:
#         print("TU BLOK FINALLY")


lista=[]
while True:

    while True:
        try:
            num=int(input("Podaj liczbe całkowitą"))
            lista.append(num)
            break
        except Exception as e:
            print(f"Błąd {e}")

    while True:
        try:
            num=float(input("Podaj liczbe rzeczywista"))
            lista.append(num)
            break
        except Exception as e:
            print(f"Błąd {e}")

    while True:
        try:
            num=int(input("Podaj index do wyswietlenia"))
            print(f"{num}: {lista[num]}")
            break
        except Exception as e:
            print(f"Błąd {e}")