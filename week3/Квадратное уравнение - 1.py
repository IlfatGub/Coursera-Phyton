# Квадратное уравнение - 1
import math
a = float(input())
b = float(input())
c = float(input())
di = b**2 - 4 * a * c
if di > 0:
    x1 = (-b + math.sqrt(di)) / (2 * a)
    x2 = (-b - math.sqrt(di)) / (2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
        print(x1, x2)
elif di == 0:
    x = -b / (2 * a)
    print(x)
