import math
a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
delta = b**2 - 4 * a * c
if (delta >= 0 and a != 0):
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}")
else:
    print("Impossivel calcular")