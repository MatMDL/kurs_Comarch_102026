# class Auto:
#     def __init__(self,marka,model):
#         self.marka=marka
#         self.model=model
#         self.predkosc=0
#     def przyspiesz(self):
#         self.predkosc+=10

#     def __eq__(self, other):
#         if not isinstance(other, Auto):
#             return NotImplemented
#         return self.marka == other.marka and self.model == other.model

#     def __hash__(self):
#         return hash((self.marka, self.model))

# bmw = Auto("BMW","X5")
# mazda = Auto("Mazda","5")
# fiat=Auto("Fiat","500")

# print(bmw)

class Zawodnik:
    def __init__(self,imie,wzrost,waga):
        self.imie=imie
        self.wzrost=wzrost
        self.waga=waga
    def BMI(self)->float:
        return ((self.waga / self.wzrost)**2)
    
    # def __eq__(self, other):
    #     if not isinstance(other, Zawodnik):
    #         return NotImplemented
    #     return self.imie == other.imie and self.imie == other.imie
    # def __hash__(self):
    #     return hash((self.imie))
    # def __str__(self):
    #     return (self.imie)


z1=Zawodnik("AAA",190,90)
z2=Zawodnik("BBB",200,200)
print(z1.BMI(), z2.BMI())
        