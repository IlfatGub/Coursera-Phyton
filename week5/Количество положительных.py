# Количество положительных
s = input()
a = [int(s) for s in s.split()]
t = 0
for i in a:
    if int(i) > 0:
        t += 1
print(t, end=' ')
