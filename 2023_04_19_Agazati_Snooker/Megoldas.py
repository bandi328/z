class Megoldas:
    eredmenyek = []
    def __init__(self):
        f = open("snooker.txt", "r", encoding="utf-8")
        f.readline()
        for sor in f:
            self.eredmenyek.append(sor.strip().split(";"))
        f.close()

    def Bevetel(self):
        atlag = []
        for eredmeny in self.eredmenyek:
            atlag.append(int(eredmeny[3]))
        print(f"4. feladat: A versenyzől átlagosan {round(sum(atlag)/len(atlag), 2)} fontot kerestek")

    def LegjobbKinai(self):
        max = 0
        index = 0
        for i in range(len(self.eredmenyek)):
            if int(self.eredmenyek[i][3]) > max:
                if self.eredmenyek[i][2] == "Kína":
                    max = int(self.eredmenyek[i][3])
                    index = i
        print(f"5. feladat: A legjobban kereső kínai versenyző:\n\tHelyezés: {self.eredmenyek[index][0]}\n\tNév: {self.eredmenyek[index][1]}\n\tOrszág: {self.eredmenyek[index][2]}\n\tNyeremény összege: {int(self.eredmenyek[index][3])*380} Ft")

    def Norveg(self):
        for eredmeny in self.eredmenyek:
            if eredmeny[2] == "Norvégia":
                print("6. feladat: A versenyzők között van norvég versenyző.")
                return
    
    def Stat(self):
        print(f"7. feladat: Statisztika")
        stat = {}
        for eredmeny in self.eredmenyek:
            if eredmeny[2] in stat.keys():
                stat[eredmeny[2]] += 1
            if eredmeny[2] not in stat.keys():
                stat[eredmeny[2]] = 1
        for key, value in stat.items():
            if value > 4:
                print(f"\t{key} - {value}")