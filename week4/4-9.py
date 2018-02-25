# Сократите дробь
a = int(input())
b = int(input())
def ReduceFraction(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a)
p = a // ReduceFraction(a, b)
q = b // ReduceFraction(a, b)
print(p, q)
