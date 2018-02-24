# Длина последовательности
max = 0
index = 1
element = - 1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        max_index = index
    index += 1
print(max_index)
