import json

with open("uczestnicy_50.json","r",encoding="utf8") as f:
    dane = json.load(f)

print(dane)
print("*"*50)
suma=0
for x in dane:
    print(f"Imie: {x["imie"]}, punkty: {x["punkty"]}")
    suma+=int(x["punkty"])

avg = suma / len(dane)
print(f"\nśrednia: {avg}")

print("\nCo najmniej 70pkt:")
for x in dane:
    if int(x["punkty"]) >= 70:
        print(f"Imię: {x['imie']}, punkty: {x['punkty']}")
    