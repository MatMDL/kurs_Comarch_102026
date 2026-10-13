
zbior={"jeden":1,"dwa":2,"trzy":3,"cztery":4,"piec":5}

num1 = input("Podaj 1 liczbe: ")
num2 = input("Podaj 2 liczbe: ")

print(num1 in zbior.keys())
print(num2 in zbior.keys())

if (num1 in zbior.keys()) and (num2 in zbior.keys()):
    print(f"Suma: {zbior.get(num1)+zbior.get(num2)}")