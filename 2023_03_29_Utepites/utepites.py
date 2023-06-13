from megoldas import *

m = Megoldas()
sorszam = int(input("2. feladat: Adja meg a jármű sorszámát: "))
print(f"\tA {sorszam}. jármű a(z) {m.Keres(sorszam)} irányba haladt!")
print(f"3. feladat: A két utolsó F felé menő jármű {m.KulonbsegSzamol()} különbséggel lépett az útra.")
stat = m.StatKeszit()
print("4. feladat:")
for key,value in stat.items():
    print(f"\t{key} óra:\tF felé: {value[0]}\tA felé:{value[1]}")
leg = m.GetLeggyorsabbak()
for i in range(0, len(leg)):
    print(f"{i+1}.: {leg[i].Idopont.time()}\t{leg[i].Honnan}\t{leg[i].Sebesseg:.2f} m/s")