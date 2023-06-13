class Keres:
    def __init__(self, sor):
        adatok = sor.strip().split("*")
        self.Cim = adatok[0]
        self.DatumIdo = adatok[1]
        self.Get = adatok[2]
        self.HttpKod = adatok[3].split(" ")[0]
        self.Meret = adatok[3].split(" ")[1]