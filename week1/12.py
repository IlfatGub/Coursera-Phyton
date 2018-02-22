a = int(input())
b = int(input())
n = int(input())
rk = b * n // 100
r = (a * n + rk)
k = b * n - rk * 100
print(r, k)
