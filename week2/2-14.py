# Список квадратов
n = int(input())
j = 1
i = 0
while True:
    i = j ** 2
    j = j + 1
    if i > n:
        break
    print(i)

