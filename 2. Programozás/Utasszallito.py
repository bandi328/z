from Sebessegkategoria import *

class Utasszallito:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.Tipus = adatok[0]
        self.Ev = int(adatok[1])
        self.Utas = adatok[2]
        self.UtasSzam = int(adatok[2].split("-")[-1])
        self.Szemelyzet = adatok[3]
        self.SzemelyzetSzam = int(adatok[3].split("-")[-1])
        self.Utazosebesseg = int(adatok[4])
        self.Felszallotomeg = int(adatok[5])
        self.Fesztav = float(adatok[6].replace(",", "."))
        sbKat = Sebessegkategoria(self.Utazosebesseg)
        self.Kategoria = sbKat.Kategorianev()