# Ряд - 2
a = int(input())
b = int(input())
def up(a, b):
    for i in range(a, b + 1, 1):
        print(i)
def down(a, b):
    for i in range(a, b - 1, -1):
        print(i)
if a < b:
    up(a, b)
else:
    down(a, b)
