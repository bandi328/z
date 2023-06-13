import random
print("2. feladat: Halmaz-e?")

lista = []
tobbszor = True
for i in range(8):
    for j in range(5):
        Random = random.randint(0, 9)
        if Random in lista:
            tobbszor = False
        lista.append(Random)
    if tobbszor == True:
        print(f"{i+1}. {lista} -> Halmaznak tekinthető")
    else:
        print(f"{i+1}. {lista} -> Halmaznak nem tekinthető")
    lista = []
    tobbszor = True