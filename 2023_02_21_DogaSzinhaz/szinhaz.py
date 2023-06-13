from megoldas import *

m = Megoldas()
sor = int(input("Adja meg a sor számát: "))
oszlop = int(input("Adja meg az oszlop számát: "))
if m.FoglaltCheck(sor, oszlop):
    print(f"2.Feladat: A {sor}. sor {oszlop}-ik széke foglalt!")
else:
    print(f"2.Feladat: A {sor}. sor {oszlop}-ik széke NEM foglalt!")
eladott = m.AranySzamol()
print(f"3.Feladat: Az előadásra eddig {eladott[1]} jegyet adtak el, ez a nézőtér {eladott[0]}%-a. ")
print(f"4.Feladat: A legtöbb jegyet a(z) {m.KategoriaSzamol()}. árkategóriában értékesítették. ")
print(f"5.Feladat: A színház össz bevétele: {m.ArSzamol()} Ft")
print(f"6.Feladat: A lonely ülőhelyek száma: {m.GetLonely()}")
m.FajlIr()