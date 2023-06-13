from auto import *

class Megoldas:
    autok = []
    def __init__(self):
        self.FajlOlvas()

    def FajlOlvas(self):
        f = open("forgalom.txt", "r", encoding="utf-8")
        f.readline()
        for sor in f:
            self.autok.append(Auto(sor))
        f.close()

    def Keres(self, sorsz):
        if self.autok[sorsz].Honnan == "F":
            return "A"
        return "F"

    def KulonbsegSzamol(self):
        felsoFele = []
        for auto in self.autok:
            if auto.Honnan == "A":
                felsoFele.append(auto)
        return int((felsoFele[-1].Idopont-felsoFele[-2].Idopont).total_seconds())
    
    def StatKeszit(self):
        stat = {}
        for auto in self.autok:
                if auto.Idopont.hour in stat.keys():
                    if auto.Honnan == "F":
                        stat[auto.Idopont.hour][0]+=1
                    else:
                        stat[auto.Idopont.hour][1]+=1
                else:
                    lista = [1,0] if auto.Honnan == "F" else [0,1]
                    stat[auto.Idopont.hour] = lista
        return stat
    
    def GetLeggyorsabbak(self):
        leg = []
        while len(leg) != 10:
            max = self.autok[0]
            for auto in self.autok:
                if auto.Sebesseg > max.Sebesseg and auto not in leg:
                    max = auto
            leg.append(max)
        return leg
    
    def FajlIr(self):
        f = open("also.txt", "w", encoding="utf-8")
        for i in range(0,len(self.autok)):
            if self.autok[i].Honnan == "F":
                kilepes = self.autok[i].Kilepes
                for j in range(i+1, len(self.autok)):
                    if self.autok[i].Kilepes > self.autok[j].Kilepes:
                        kilepes = self.autok[j].Kilepes
                f.write(f"{str(kilepes.time())}\n")
        f.close()