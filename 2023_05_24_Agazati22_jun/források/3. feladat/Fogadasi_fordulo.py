class Fogadasi_fordulo:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.Ev = adatok[0]
        self.Hét = adatok[1]
        self.Fordulo = adatok[2]
        self.T13p1 = int(adatok[3])
        self.Ny13p1 = adatok[4]
        self.Eredmenyek = adatok[5]