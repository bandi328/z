nev = input("Diák neve: ")
evvegi = []
osztalyzatok = ["elégtelen", "elégséges", "közepes", "jó", "jeles"]
for i in range(5):
    osszeg = 0
    tantargy = input(f"{i+1}. tantárgy neve: ")
    jegyek = input(f"\t{tantargy.capitalize()} jegyek: ")
    for jegy in jegyek:
        osszeg += int(jegy)
    print(f"\tÁtlag: {int(osszeg/len(jegyek))}")
    jegy = int(round(osszeg/len(jegyek), 0))
    print(f"\tÉv végi jegy: {jegy} ({osztalyzatok[jegy-1]})")
    evvegi.append(jegy)
ev = sum(evvegi)/len(evvegi)
print(f"{nev} év végi átlaga: {ev}")
if ev >= 2.00 and ev <= 2.99:
    print("Jövő évi várható ösztöndíja: 8.000 Ft")
elif ev >= 3.00 and ev <= 3.99:
    print("Jövő évi várható ösztöndíja: 25.000 Ft")
elif ev >= 4.00 and ev <= 4.49:
    print("Jövő évi várható ösztöndíja: 42.000 Ft")
elif ev > 4.49:
    print("Jövő évi várható ösztöndíja: 59.000 Ft")