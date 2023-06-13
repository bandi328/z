from Megoldas import *

m = Megoldas()
m.FajlOlvas()
print(f"5.feladat: Karakterek száma: {m.GetHossz()}")
kar = m.GetKar()
keresett = m.Keres(kar)
print("7.feladat:")
if keresett != None:
    keresett.MatrixKiir()
else:
    print("Nincs ilyen karakter a bankban!")
m.FajlOlvas(m.Dekodolando, "dekodol.txt")