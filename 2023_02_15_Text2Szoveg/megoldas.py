from IdozitettFelirat import *

class Megoldas():

    feliratok = []

    def FajlOlvas(self):
        f = open("feliratok.txt", "r", encoding="utf-8")
        index = 1
        for sor in f:
            if index % 2 == 0:
                self.feliratok.append(IdozitettFelirat(idobelyeg.strip(), sor.strip()))
            else:
                idobelyeg = sor
            index += 1
        f.close()

    def GetSorokSzama(self):
        return len(self.feliratok)

    def MaxKeres(self):
        maxFelirat = self.feliratok[0]
        for felirat in self.feliratok:
            if felirat.SzavakSzama() > maxFelirat.SzavakSzama():
                maxFelirat = felirat
        return maxFelirat.Felirat
    
    def FajlIr(self):
        f = open("felirat.srt", "w", encoding="utf-8")
        for i in range(len(self.feliratok)):
            f.write(f"{i+1}\n{self.feliratok[i].SrtIdozites()}\n{self.feliratok[i].Felirat}\n\n")
        f.close()