import random
nevek = []
nevek.append(input("Első játékos neve: "))
nevek.append(input("Második játékos neve: "))
elso = masodik= 0
index = 1

while elso + masodik != 12:
    print(f"{index}. kör:")
    for nev in nevek:
        elso = random.randint(1, 6)
        masodik = random.randint(1, 6)
        print(f"{nev} dobása: {elso} + {masodik}")
        if elso+masodik == 12:
            print(f"A játékot {nev} kezdheti.")
    index += 1
