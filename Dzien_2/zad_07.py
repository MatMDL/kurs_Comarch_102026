def potega(a,b):
    if b==0:
        return 1
    while b>1:
        a+=a
        b-=1
    return a

print(potega(2,5))
# ********************************
def potega2(a,b):
    if b>0:
        return a*potega2(a,b-1)
    else:
        return 1

print(potega2(2,5))
print(potega2(2,-1))
# ********************************
# from typing import Annotated, get_type_hints

# def greet(name: Annotated[str, "IMIE"]):
#     """TEST"""
#     return(f"Czesc, {name}")

# print(greet("AAA"))
# print(greet(12))
# print(get_type_hints(greet,include_extras=True))
# ********************************
def silnia(a):
    if a>0:
        return a*silnia(a-1)
    else:
        return 1

for i in range(1,10):
    print(silnia(i))