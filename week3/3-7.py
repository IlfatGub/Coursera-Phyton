# Квадратное уравнение - 1
import math
a = float(input())
b = float(input())
c = float(input())
z = b * b - 4 * a * c
d = math.sqrt(z)
x1 = 0
x2 = 0
if d > 0:
    x1 = ((-b) + d)/(2 * a)
    x2 = ((-b) - d)/(2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
    print(round(x1, 6), round(x2, 6))
elif d == 0:
    x12= (-b)/(2 * a)
    print(round(x12))


