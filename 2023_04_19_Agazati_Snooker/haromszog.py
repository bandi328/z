print("1. feladat: A háromszög szerkeszthetősége\nKérem a háromszög oldalait!")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a+b>c and c+b>a and a+c>b:
    print("A háromszög szerkeszthető!")
else:
    print("A háromszög nemszerkeszthető meg a megadott adatokkal!")