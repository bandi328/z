from Keres import *

class Megoldas:
    keres = []
    def __init__(self):
        f = open("NASAlog.txt", "r", encoding="utf-8")
        for i in f:
            self.keres.append(Keres(i))
        f.close()

    def ByteMeret(self):
        byte = 0
        for keres in self.keres:
            if keres.Meret == "-":
                byte += 0
            else:
                byte += int(keres.Meret)
        return byte
    
    def Domain(self, ugyfel):
        if ugyfel[-1].isnumeric() == True:
            return False
        else:
            return True
    
    def Domaines(self):
        domaines = 0
        for keres in self.keres:
            if self.Domain(keres.Cim) == True:
                domaines += 1
        print(f"8. feladat: Domain-es kérések: {round(domaines/len(self.keres)*100, 2)}%")

    def Stat(self):
        stat = {}
        for keres in self.keres:
            if keres.HttpKod not in stat.keys():
                stat[keres.HttpKod] = 1
            elif keres.HttpKod in stat.keys():
                stat[keres.HttpKod] += 1
        print("9. feladat: Statisztika:")
        for key, value in stat.items():
            print(f"\t{key}: {value} db")