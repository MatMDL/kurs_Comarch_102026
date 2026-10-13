# import random

# while True:
#     los = random.randint(1,10)
#     print(los)
#     if los == 6:
#         break

import random
los = random.randint(1,100)
proby=0

while True:
    proby+=1
    if proby>3:
        print("Wykorzystano limit prób")
        break
    num=int(input("Podaj liczbe: "))
    if num<los:
        print("Za mała")
    elif num>los:
        print("Za duża")
    else:
        print("Wygrana")
        break