import math

while True:
    try:
        m = float(input("m = "))
        v = float(input("v = "))
    except:
        print("Nem számot adott meg.")
        continue
    try:
        print(f"x = {round(((math.sqrt(math.sqrt(m+v)*math.pi)/(2*math.pi))**(8/5))*(1/2*v), 2)}")
        break
    except:
        print("A gyökjel alatt negatív szám van.")