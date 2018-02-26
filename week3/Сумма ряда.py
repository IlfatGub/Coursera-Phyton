# Сумма ряда
n = int(input())
i = 1
s = 1
while i < n:
    i = i + 1
    s = s + 1 / i ** 2
print(round(s, 5))
