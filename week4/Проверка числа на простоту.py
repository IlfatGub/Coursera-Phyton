# Проверка числа на простоту
def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    if d * d > n:
        return True
    else:
        return False


def val(n):
    if IsPrime(n):
        return "YES"
    else:
        return "NO"

n = int(input())
print(val(n))
