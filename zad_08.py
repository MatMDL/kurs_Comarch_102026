num1 = int(input("Podaj 1 liczbe: "))
znak = input("Podaj znak: ")
num2 = int(input("Podaj 2 liczbe: "))

match znak:
    case "+":
        print(f"Wynik: {num1+num2}")
    case "-":
        print(f"Wynik: {num1-num2}")
    case "*":
        print(f"Wynik: {num1*num2}")
    case "/":
        print(f"Wynik: {num1/num2}")
    case _:
        "Błędny znak"