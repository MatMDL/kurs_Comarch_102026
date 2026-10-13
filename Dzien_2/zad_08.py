potega = lambda x, a : x**a
print(potega(2,5))
print(potega(2,-1))

parzysta = lambda x : True if x%2==0 else False
print(parzysta(11))

# ******************************

# ITERATOR
dane =[11,22,33,44]
it = iter(dane)
for i in range(4):
    print(next(it))

# GENERATOR
def liczby(n):
    for i in range(1,n+1):
        yield i

x = liczby(5)
for i in range(5):
    print(next(x))

# ******************************
def parzysta2(s,k):
    for l in range(s,k):
        if l%2==0:
            yield l

gen = parzysta2(1,20)
for x in gen:
    print(x)
# ******************************
print(40*"*")