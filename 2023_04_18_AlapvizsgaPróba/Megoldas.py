from CBadas import *

class Megoldas:
    adasok = []
    def __init__(self):
        f = open("cb.txt", "r", encoding="utf-8")
        f.readline()
        for sor in f:
            self.adasok.append(CBadas(sor))
        f.close()

    def Sanyi(self):
        index = 0
        for adas in self.adasok:
            if adas.Nev == "Sanyi":
                index += 1
        return index
    
    def EgyPerc(self):
        print("3.4 feladat: A legtöbb adás:")
        max = 0
        for adas in self.adasok:
            if adas.AdasDb > max:
                max = adas.AdasDb
        for adas in self.adasok:
            if max == adas.AdasDb:
                print(f"\tIdő: {adas.Ora}:{adas.Perc} Darab: {adas.AdasDb} Név: {adas.Nev}")

    def FajlIras(self):
        f = open("cb2.txt", "w", encoding="utf-8")
        f.write(f"Kezdes;Nev;AdasDb\n")
        for adas in self.adasok:
            f.write(f"{(adas.Ora*60)+adas.Perc};{adas.Nev};{adas.AdasDb}\n")