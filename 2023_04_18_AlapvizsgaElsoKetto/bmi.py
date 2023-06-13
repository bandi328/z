suly = int(input("Kérem a súlyt kilobramban: "))
cm = int(input("Kérem a súlyt cm-ben: "))
m = cm/100
TTI = suly/(m*m)
print(f"A testtömeg indexe: {round(TTI, 2)}")

if TTI < 16:
    print("A testsúly osztálya: súlyos soványság")
elif TTI >= 16 and TTI <=18.49:
    print("A testsúly osztálya: soványság")
elif TTI >= 15.5 and TTI <= 24.99:
    print("A testsúly osztálya: normális")
elif TTI >= 25 and TTI <= 29.99:
    print("A testsúly osztálya: túlsúlyos")
else:
    print("A testsúly osztálya: elhízás")