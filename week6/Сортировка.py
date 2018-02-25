# Сортировка
n = int(input())
i = 0
a = ''
while i != n:
    a = a + str(input())
    i += 1
a = sorted(a.split())
print(' '.join(map(str, a)))