class Ar:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.Datum = adatok[0].split(".")
        self.Benzin = int(adatok[1])
        self.Gazolaj = int(adatok[2])