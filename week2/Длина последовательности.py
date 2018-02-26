n = int(input())
num = 0
i = 0
while n != 0:
    n = int(input())
    i += 1
    while n == 0:
        num = i
        break
    continue
print(num)
