from Fogadasi_fordulo import *

totok = []
def FajlOlvas():
    f = open("toto.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        totok.append(Fogadasi_fordulo(sor))
    f.close()

print("3. feladat: Toto")
print(f"3.1 feladat: Adatok beolvasása és tárolása{FajlOlvas()}")
print(f"3.2 feladat: Fogadási fordulók száma: {len(totok)}")

db = 0
for toto in totok:
    db += toto.T13p1
print(f"3.3 feladat: Telitalálatos szelvények száma: {db} darab")

for toto in totok:
    eredmeny = toto.Eredmenyek.split()
    for i in eredmeny:
        if "X" == i:
            break
    else:
        print("3.4 feladat: Volt döntetlen mentes forduló!")
        break
else:
    print("3.4 feladat: Nem volt döntetlen mentes forduló!")