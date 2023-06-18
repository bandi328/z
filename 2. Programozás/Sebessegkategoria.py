class Sebessegkategoria:
    Utazosebesseg = None
    def __init__(self, utazosebesseg):
        self.Utazosebesseg = utazosebesseg

    def Kategorianev(self):
        if self.Utazosebesseg < 500:
            return "Alacsony sebességű"
        elif self.Utazosebesseg < 1000:
            return "Szubszonikus"
        elif self.Utazosebesseg < 1200:
            return "Transzszonikus"
        else:
            return "Szuperszonikus"
