import math
import os
os.system("cls")
print("Mach-szám kalkulátor")

qc = input("Torlónyomás: ")
p0 = input("Statikus nyomás: ")

while qc != "":
    while qc.replace('.', '', 1).isnumeric() == False and p0.replace('.', '', 1).isnumeric() == False:
        print("Nem megfelelő a bemeneti karakterlánc formátuma.")
        
        qc = input("Torlónyomás: ")
        p0 = input("Statikus nyomás: ")

    Ma = math.sqrt(5*((((float(qc)/float(p0))+1)**(2/7))-1))
    if Ma < 1:
        print(Ma)

    qc = input("Torlónyomás: ")
    if qc == "":
        break
    p0 = input("Statikus nyomás: ")