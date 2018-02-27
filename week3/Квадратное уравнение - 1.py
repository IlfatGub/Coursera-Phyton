# Квадратное уравнение - 1
import math
a = float(input())
b = float(input())
c = float(input())
di = (b**2) - (4 * a * c)
if di > 0:
    x1 = ((-1) * b + math.sqrt(di)) / (2 * a)
    x2 = ((-1) * b - math.sqrt(di)) / (2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
        print(round(x1, 6), round(x2, 6))
elif di == 0:
    x = -b / 2 / a
    print(x)
else:
    print()


