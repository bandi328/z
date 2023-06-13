beker = input("Kérek egy szövegete: ")
while beker != "VÉGE":
    szoveg = beker.strip().split(" ")
    kiir = ""
    for szo in szoveg:
        for j in range(1, len(szo)+1):
            kiir += szo[-j]
        kiir += " "
    print(kiir)
    beker = input("Kérek egy szövegete: ")