def test(*args):
    print(args)

test(1,2)
test(1,2,3,4,5,6,7,8,9)
test(1,2,3,4,5)
test(1,2,3,4,5,6,7,8,9,10,11,12,13)

def test2(**kwargs):
    print(kwargs)

test2(a=1,b=2)
test2(a=1,b=2,c=5.5)
test2(a=1,b=2,c=5.5,d="test")

print(40*"*")

#scope
ile = 0
def test3():
    ile=0
    ile+=1
    print(ile)
test3()
print(ile)

ile2 = 0
def test4():
    global ile2
    ile2+=1
    print(ile2)
test4()
print(ile2)