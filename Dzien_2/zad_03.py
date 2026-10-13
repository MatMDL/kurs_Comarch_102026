nums=[]
for i in range(5):
    nums.append(int(input(f"Podaj liczbe {i+1}: ")))

slownik={}
for i in nums:
    if i in slownik:
        slownik[i]+=1
    else:
        slownik[i]=1

print(slownik)