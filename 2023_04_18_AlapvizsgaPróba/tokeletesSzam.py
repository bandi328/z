def Tokeletes(szam):
    osztok = []
    for oszto in range(tol, ig+1):
        if szam != oszto:
            if szam%oszto == 0:
                osztok.append(oszto)
    if szam == sum(osztok):
        return True
    return False
            
print(f"2. feladat: Tökéletes számok")

tol = int(input("elso  "))
ig = int(input("masodik  "))
szamok = []
for i in range(tol, ig+1):
    if Tokeletes(i):
        szamok.append(i)
elem = ""
for szam in szamok:
    elem += f"{str(szam)}; "
print(elem[:-2])