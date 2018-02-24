# Количество элементов, равных максимуму
m = 0
num_m = 0
element = -1
while element != 0:
    element = int(input())
    if element > m:
        m, num_m = element, 1
    elif element == m:
        num_m += 1
print(num_m)
