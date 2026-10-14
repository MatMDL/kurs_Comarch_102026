import json
# sklep={"kiwi":1.11,"banan":[2.22,3.33]}

# with open("Testowy.json","w",encoding="utf8") as f:
#     json.dump(sklep,f)
 
with open("Testowy.json","r",encoding="utf8") as f:
    dane = json.load(f)

print(dane, type(dane))


import pickle

# sklep={"kiwi":1.11,"banan":[2.22,3.33]}
# with open("Testowy.dat","wb") as f:
#     pickle.dump(sklep,f)

with open("Testowy.dat","rb") as f:
    dane = pickle.load(f)

print(dane, type(dane))