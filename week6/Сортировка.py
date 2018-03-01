# Сортировка
n = int(input())
a = list(map(int, input().split()))
c = []
i = 0
if len(a) > n:
    while i <= n - 1:
        c.append(a[i])
        i += 1
elif len(a) < n:
    while i <= len(a) - 1:
        c.append(a[i])
        i += 1
else:
    while i != n:
        c.append(a[i])
        i += 1

print(' '.join(map(str, sorted(c))))
