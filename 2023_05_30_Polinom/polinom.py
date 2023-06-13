szamok = None
beker = input("Adjon meg egész számokat: ")
while beker != "":
    szamok = beker.split(" ")
    if len(szamok) > 4:
        print("Négynél több számot adott meg.")
        while len(szamok) != 4:
            szamok.pop()
    elif len(szamok) < 4:
        while len(szamok) != 4:
            szamok.append(0)
    
    f = open("eh.txt", "a", encoding="utf-8")
    f.write(f"{szamok[3]}x^3+{szamok[2]}x^2+{szamok[1]}x+{szamok[0]}=y\n")

    beker = input("Adjon meg egész számokat: ")
f.close()