from fgvk import *

megoldas = []
azonositok = []
valaszok = []

FajlOlvas(megoldas, azonositok, valaszok)
print("1. feladat: Az adatok beolvasása")
print(f"2. feladat: A vetélkedőn {len(azonositok)} versenyző indult.")
beker = bekerAzonosito(azonositok, valaszok)
print(f"{beker}\t(a versenyző válasza)")
helyesValasz(megoldas, beker)
egyHelyesValasz(megoldas, valaszok)
print("6. feladat: A versenyzők pontszámának meghatározása")
pontszam(megoldas, azonositok, valaszok)
legjobb()