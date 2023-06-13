from megoldas import *

m = Megoldas()
m.FajlOlvas()
print(f"5.feladat: Feliratok száma: {m.GetSorokSzama()}")
print(f"7.feladat: Legtöbb szóból álló felirat:\n{m.MaxKeres()}")
m.FajlIr()