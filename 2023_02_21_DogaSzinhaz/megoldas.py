class Megoldas:
    foglaltsag = []
    kategoria = []
    def __init__(self) -> None:
       self.FajlOlvas("foglaltsag.txt", self.foglaltsag)
       self.FajlOlvas("kategoria.txt", self.kategoria)

    def FajlOlvas(self, fajlnev, lista):
        f = open(fajlnev, "r", encoding="utf-8")
        for sor in f:
            lista.append(sor.strip())
        f.close()

    def FoglaltCheck(self, sor, oszlop):
        if self.foglaltsag[sor-1][oszlop-1] == 'x':
            return True
        return False
    
    def AranySzamol(self):
        db = 0
        ossz = 0
        for sor in self.foglaltsag:
            ossz += len(sor)
            for szek in sor:
                if szek == 'x':
                    db+=1
        return int(round(db/ossz*100, 0)), db

    def KategoriaSzamol(self):
        stat = {}
        for i in range(len(self.kategoria)):
            for j in range(len(self.kategoria[i])):
                if self.foglaltsag[i][j] == 'x':
                    if self.kategoria[i][j] in stat.keys():
                        stat[self.kategoria[i][j]]+=1
                    else:
                        stat[self.kategoria[i][j]] = 1
        max = 0
        maxKat = 0
        for key, value in stat.items():
            if value > max:
                max = value
                maxKat = key
        return maxKat

    def ArSzamol(self):
        ossz = 0
        for i in range(len(self.foglaltsag)):
            for j in range(len(self.foglaltsag[i])):
                if self.foglaltsag[i][j] == 'x':
                    if self.kategoria[i][j] != '5':
                        ossz += 6000 - int(self.kategoria[i][j])*1000
                    else:
                        ossz += 1500
        return ossz

    def GetLonely(self):
        db = 0
        for i in range(len(self.foglaltsag)):
            if self.foglaltsag[i][0] == 'o' and self.foglaltsag[i][1] == 'x':
                db += 1
            if self.foglaltsag[i][-1] == 'o' and self.foglaltsag[i][-2] == 'x':
                db += 1 
            for j in range(1,len(self.foglaltsag[i])-1):
                if self.foglaltsag[i][j] == 'o' and self.foglaltsag[i][j-1] == 'x' and self.foglaltsag[i][j+1] == 'x':
                    db += 1
        return db

    def FajlIr(self):
        f = open("szabad.txt", "w", encoding="utf-8")
        for i in range(len(self.foglaltsag)):
            for j in range(len(self.foglaltsag[i])):
                if self.foglaltsag[i][j] == "x":
                    f.write("x")
                else:
                    f.write(self.kategoria[i][j])
            f.write("\n")
        f.close()