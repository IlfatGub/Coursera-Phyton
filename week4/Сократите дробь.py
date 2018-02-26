# Сократите дробь
import math

a = int(input())
b = int(input())


def ReduceFraction(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a)
k = ReduceFraction(a, b)
print(a // k, b // k)
