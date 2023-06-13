class Karakter:
    def __init__(self, betu):
        self.Kar = betu
        self.Matrix = []

    def MatrixKiir(self):
        for sor in self.Matrix:
            print(sor)

    def Felismer(self, dekMatrix):
        if self.Matrix == dekMatrix:
            return True
        return False