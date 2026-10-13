def generuj_bilety(s,k):
    for numer in range(s,k+1):
        yield numer

bilety = generuj_bilety(100,105)
print(next(bilety))
print(next(bilety))
print(next(bilety))
print(next(bilety))

print(50*"*")

transakcje = [
    {"id": 1, "typ": "wpłata", "kwota": 1500},
    {"id": 2, "typ": "wypłata", "kwota": 200},
    {"id": 3, "typ": "wypłata", "kwota": 800},
    {"id": 4, "typ": "wpłata", "kwota": 300},
    {"id": 5, "typ": "wypłata", "kwota": 1200},
    {"id": 6, "typ": "wpłata", "kwota": 2500},
    {"id": 7, "typ": "wypłata", "kwota": 100},
    {"id": 8, "typ": "wypłata", "kwota": 600}
]

def filtruj_transakcje(transakcje, typ, min_kwota):
    for transakcja in transakcje:
        if typ==transakcja["typ"] and min_kwota<=transakcja["kwota"]:
            yield transakcja

generator = filtruj_transakcje(transakcje, "wypłata",500)
for transakcja in generator:
    print(transakcja)