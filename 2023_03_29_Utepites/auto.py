import datetime

class Auto:
    def __init__(self, sor):
        adatok = sor.strip().split()
        self.Idopont = datetime.datetime(1, 1, 1, int(adatok[0]), int(adatok[1]), int(adatok[2]))
        self.Idotartam = int(adatok[3])
        self.Honnan = adatok[4]
        self.Sebesseg = self.Idotartam
        self.Kilepes = self.Idopont + datetime.timedelta(0, self.Idotartam)