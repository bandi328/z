class IdozitettFelirat:
    def __init__(self, ido, felirat):
        self.Ido = ido
        self.Felirat = felirat

    def SzavakSzama(self):
        return len(self.Felirat.split())

    def SrtIdozites(self):
        eredmeny = ""
        idoDb = self.Ido.split(" - ")
        for i in range(len(idoDb)):
            idok = idoDb[i].split(":")
            osszmp = int(idok[0])*60 + int(idok[1])
            orak = int(osszmp / 3600)
            perc = int((osszmp - orak * 3600) / 60)
            mp = osszmp - ((orak * 3600) + (perc * 60))
            eredmeny += f"0{orak}:"
            if perc < 10:
                eredmeny += f"0{perc}"
            else:
                eredmeny += str(perc)
            if mp < 10:
                eredmeny += f":0{mp}"
            else:
                eredmeny += f":{mp}"
            if i == 0:
                eredmeny += " --> "
        return eredmeny