# liczba=10
# if (liczba>0) and liczba%2==0:
#     print("Podzielna")



num1 = int(input("Podaj 1 liczbe: "))
num2 = int(input("Podaj 2 liczbe: "))
num3 = int(input("Podaj 3 liczbe: "))
num4 = int(input("Podaj 4 liczbe: "))
num5 = int(input("Podaj 5 liczbe: "))

max=num1
min=num1

if num2 < min:
    min = num2
if num2 > max:
    max = num2

if num3 < min:
    min = num3
if num3 > max:
    max = num3

if num4 < min:
    min = num4
if num4 > max:
    max = num4

if num5 < min:
    min = num5
if num5 > max:
    max = num5

print(f"Max: {max}, Min: {min}")

    