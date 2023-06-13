from Ar import *

def FajlOlvas(lista):
    f = open("uzemanyag.txt", "r", encoding="utf-8")
    for sor in f:
        lista.append(Ar(sor.strip()))
    f.close()

def legkisebb(lista):
    min = abs(lista[0].Benzin-lista[0].Gazolaj)
    for i in range(1, len(lista)):
        if abs(lista[i].Benzin-lista[i].Gazolaj) < min:
            min = abs(lista[i].Benzin-lista[i].Gazolaj)
    return min

def legkisebbDb(lista):
    db = 0
    for i in range(1, len(lista)):
        if abs(lista[i].Benzin-lista[i].Gazolaj) == legkisebb(lista):
            db += 1
    return db

def szokoev(lista):
    for i in range(len(lista)):
        if int(lista[i].Datum[0])%4 == 0:
            if lista[i].Datum[1] == "02" and lista[i].Datum[2] == "24":
                if abs(lista[i].Benzin-lista[i].Gazolaj) != 0:
                    print("6. feladat: Volt változás szökőnapon!")

def euro(lista):
    f = open("euro.txt", "w", encoding="utf-8")
    for i in range(len(lista)):
        f.write(f"{lista[i].Datum};{round(lista[i].Benzin/307.7, 2)};{round(lista[i].Gazolaj/307.7, 2)}\n")
    f.close()

def beker():
    beker = input(f"8. feladat: Kérem adja meg az évszámot [2011..2016]: ")
    while beker.isnumeric() == False:
        beker = input(f"8. feladat: Kérem adja meg az évszámot [2011..2016]: ")
    while int(beker) < 2011 or int(beker) > 2016:
        beker = input(f"8. feladat: Kérem adja meg az évszámot [2011..2016]: ")
    return beker

def napok(lista, most, elozo):
    napokSzama = {31,28,31,30,31,30,31,31,30,31,30,31}
    for i in range(len(lista)):
        datum = lista[i].Datum.strip().split(".")
        if datum[0]%4 == 0:
            napokSzama[1] = 29
    if int(most.Datum[1]) == int(elozo.Datum[1]):
        return int(most.Datum[2])-int(elozo.Datum[2])
    else:
        return napokSzama[int(elozo.Datum[1])-1] - int(elozo.Datum[2]) + int(most.Datum[2])