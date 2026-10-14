from pathlib import Path
plik = Path(__file__).parent / "data.txt"

# **************************************************
with open(plik,"r",encoding="utf8") as f:
    print(f.readline())

    dane=f.readlines()
    print(dane)
    for x in dane:
        if x.strip()=="ccc":
            print("OK")

print("AAA", end="->")  # domyślnie '/n'
print("BBB")

# **************************************************
with open(plik,"r",encoding="utf8") as f:   # read
    for l in f:
        d=l.strip().split(";")
        print(d)
# **************************************************
with open(plik,"w",encoding="utf8") as f:   # write - nadpisuje cały plik
    f.write("aaa;111;222\n")
    f.write("bbb;333;444\n")
    f.write("ccc;555;666\n")
    f.write("ddd;777;888\n")
# **************************************************
with open(plik,"a",encoding="utf8") as f:   # append
    f.write("aaa;111;222\n")
    f.write("bbb;333;444\n")
    f.write("ccc;555;666\n")
    f.write("ddd;777;888\n")