# Утренняя пробежка
x = int(input())
y = int(input())
i = 1
while True:
    i = i + 1
    x = x + x * 0.1
    if x >= y :
        print(i)
        break
