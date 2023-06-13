import math

print("1. feladat: Háromszög kerülete és területe\nKérem a háromszög oldalait")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
s = (a+b+c)/2
print(f"K = {a+b+c}")
print(f"T = {math.sqrt(s*(s-a)*(s-b)*(s-c))}")