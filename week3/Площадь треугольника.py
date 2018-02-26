# Площадь треугольника
import math
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2.0
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)
