from Megoldas import *

m = Megoldas()
m.FajlOlvas()
print(f"4. feladat: Adatsorok száma: {m.GetRepuloDb()}")
print(f"5. feladat: Boeing típusok száma: {m.GetBoeingDb()} ")
print(f"6. feladat: A legtöbb utast szállító repülőgéptípus:")
max = m.GetMaxUtas()
print(f"\tTipus: {max.Tipus}\n\tElső felszállás: {max.Ev}\n\tUtasok száma: {max.Utas}\n\tSzemélyzet: {max.Szemelyzet}\n\tUtazósebesség: {max.Utazosebesseg}")
print(f"7. feladat:\n\t{m.HianyzoKatKeres()}")
m.FajlIr()