class Slownik(dict):
    def __missing__(self, key):
        return 0

sklep = Slownik()
sklep["Kiwi"]=1.22
sklep["Jablko"]=2.22

print(sklep["Kiwi"])
