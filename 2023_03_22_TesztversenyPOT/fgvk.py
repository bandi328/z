def FajlOlvas(megoldas, azonositok, valaszok):
    f = open("valaszok.txt", "r", encoding="utf-8")
    megoldas.append(f.readline().strip())
    
    for sor in f:
        egyAdat = sor.strip().split(" ")
        azonositok.append(egyAdat[0])
        valaszok.append(egyAdat[1])
    f.close()

def bekerAzonosito(azonositok, valaszok):
    beker = input("3. feladat: A versenyző azonosítója = ")
    for i in range(len(azonositok)):
        if beker == azonositok[i]:
            return valaszok[i]

def helyesValasz(megoldas, beker):
    valasz = list(beker)
    jelzes = ""
    for i in range(len(valasz)):
        if valasz[i] == list(megoldas[0])[i]:
            jelzes += "+"
        else:
            jelzes += " "
    print(f"4. feladat:\n{megoldas[0]}\t(a helyes megoldás)\n{jelzes}\t(a versenyző helyes válaszai)")

def egyHelyesValasz(megoldas, valaszok):
    beker = int(input("5. feladat: A feladat sorszáma = "))
    db = 0
    for valasz in valaszok:
        v = list(valasz)
        if v[beker-1] == list(megoldas[0])[beker-1]:
            db += 1
    print(f"A feladatra {db} fő, a versenyzők {round((db/len(valaszok))*100, 2)}%-a adott helyes választ.")

def pontszam(megoldas, azonositok, valaszok):
    f = open("pontok.txt", "w", encoding="utf-8")
    pontszam = index = 0
    for i in range(len(valaszok)):
        for j in valaszok[i]:
            if j == list(megoldas[0])[index]:
                if index+1 < 6:
                    pontszam += 3
                elif index+1 < 11:
                    pontszam += 4
                elif index+1 < 14:
                    pontszam += 5
                elif index+1 == 14:
                    pontszam += 6
            index += 1
        f.write(f"{azonositok[i]} {pontszam}\n")
        pontszam = index = 0
    f.close()

def legjobb():
    f = open("pontok.txt", "r", encoding="utf-8")
    azonositok = []
    pontok = []
    for sor in f:
        egy = sor.strip().split(" ")
        azonositok.append(egy[0])
        pontok.append(egy[1])

    elso = 0
    for i in range(len(pontok)):
        if int(pontok[i]) > elso:
            elso = int(pontok[i])
    for i in range(len(pontok)):
        if int(pontok[i]) == elso:
            print(f"1. díj ({elso} pont): {azonositok[i]}")

    masodik = 0
    for i in range(len(pontok)):
        if int(pontok[i]) > masodik and int(pontok[i]) != elso:
            masodik = int(pontok[i])
    for i in range(len(pontok)):
        if int(pontok[i]) == masodik:
            print(f"2. díj ({masodik} pont): {azonositok[i]}")

    harmadik = 0
    for i in range(len(pontok)):
        if int(pontok[i]) > harmadik and int(pontok[i]) != elso and int(pontok[i]) != masodik:
            harmadik = int(pontok[i])
    for i in range(len(pontok)):
        if int(pontok[i]) == harmadik:
            print(f"3. díj ({harmadik} pont): {azonositok[i]}")
    print()