import random

jatekos1 = input("Adja meg a(z) 1. játékos nevét: ")
jatekos2 = input("Adja meg a(z) 2. játékos nevét: ")

pont1 = 0
pont2 = 0

kor = 1

# [0, 1, 2]
# ["ko", "papir", "ollo"]
eset1 = 0 #dontetlen
eset2 = 1 #ko + papir
eset3 = 2 #ko + ollo
eset4 = 3 #papir + ollo

while pont1 != 3 and pont2 != 3:
    elso = random.randint(0, 2)
    masodik = random.randint(0, 2)

    if elso + masodik == 0:
        print(f"{kor} kör: Döntetlen!")
elif: