from Utasszallito import *

class Megoldas:
    fejlec = None
    utasszallitok = []
    kategoriak = ["Alacsony sebességű", "Szubszonikus", "Transzszonikus", "Szuperszonikus"]
    def __init__(self):
        pass

    def FajlOlvas(self):
        f = open("utasszallitok.txt", "r", encoding="utf-8")
        self.fejlec = f.readline()
        for sor in f:
            self.utasszallitok.append(Utasszallito(sor))
        f.close()
    
    def GetRepuloDb(self):
        return len(self.utasszallitok)
    
    def GetBoeingDb(self):
        db = 0
        for repulo in self.utasszallitok:
            if "Boeing" in repulo.Tipus:
                db += 1
        return db
    
    def GetMaxUtas(self):
        max = self.utasszallitok[0]
        for repulo in self.utasszallitok:
            if repulo.UtasSzam > max.UtasSzam:
                max = repulo
        return max
    
    def HianyzoKatKeres(self):
        for repulo in self.utasszallitok:
            if repulo.Kategoria in self.kategoriak:
                self.kategoriak.remove(repulo.Kategoria)
        if len(self.kategoriak) == 0:
            return "Minden sebességkategóriából van repülőgéptípus."
        szoveg = ""
        for kat in self.kategoriak:
            szoveg += f"{kat} "
        return szoveg
    
    def FajlIr(self):
        f = open("utasszallitok_new.txt", "w", encoding="utf-8")
        f.write(f"{self.fejlec}")
        for repulo in self.utasszallitok:
            f.write(f"{repulo.Tipus};{repulo.Ev};{repulo.UtasSzam};{repulo.SzemelyzetSzam};{repulo.Utazosebesseg};{repulo.Felszallotomeg/1000:.0f};{repulo.Fesztav*3.2808:.0f}\n")
        f.close()