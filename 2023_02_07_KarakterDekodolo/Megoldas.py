from Karakter import *

class Megoldas:
    def __init__(self):
      self.Karakterek = []
      self.Dekodolando = []

    def FajlOlvas(self, lista, fajlNev):
        db = 0
        f = open(fajlNev, "r", encoding="utf-8")
        for sor in f:
            egySor = sor.strip()
            if len(egySor) == 1:
                kar = egySor
                k = Karakter(kar)
            else:
                k.Matrix.append(egySor)
                db+=1
            if db == 7:
                lista.append(k)
                db = 0
        f.close()

    def GetHossz(self):
        return len(self.Karakterek)

    def GetKar(self):
        kar = ""
        while len(kar) != 1 or (kar[0] < "A" or kar[0] > "Z"):
            kar = input("6.feladat: Kérek egy angol nagybetűt: ")
        return kar

    def Keres(self, betu):
        for karakter in self.Karakterek:
            if betu == karakter.Kar:
                return karakter
        return None

    def Dekodol(self):
        eredmeny = ""
        for dekKar in self.Dekodolando:
            for karakter in self.Karakterek:
                if karakter.Felismer(dekKar.Matrix):
                    eredmeny += karakter.Kar
                    break
            else:
                eredmeny += "?"
        return eredmeny