# Быстрое возведение в степень
x = float(input())
p = int(input())


def pow(x, p):
    if p < 0:
        p = -p
        x = 1. / x
    m = x
    t = 1
    while p:
        if p % 2:
            t *= m
        m *= m
        p //= 2
    return t

print(pow(x, p))
