class Bankomat:
    def __init__(self,nazwa,miasto):
        self.nazwa=nazwa
        self.miasto=miasto
        self.__kasa=1000000000
    def wyplac(self,pin,ile):
        if pin==1111:
            self.__kasa-=ile
        else:
            print("Błędny pin")
    def saldo(self):
        self.__saldo()
    def __saldo(self):
        print(self.__kasa)
    def getKasa(self):
        return (self.__kasa)

bankomat = Bankomat("Euronet", "Wawa")
print(bankomat.saldo(), bankomat.nazwa, bankomat.miasto)
bankomat.wyplac(1111,300)
print(bankomat.saldo(), bankomat.nazwa, bankomat.miasto)
bankomat.__kasa = 10
print(bankomat.saldo(), bankomat.nazwa, bankomat.miasto, bankomat.__kasa)