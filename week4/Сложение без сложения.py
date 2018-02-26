# Сложение без сложения
def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)
a = int(input())
b = int(input())
print(summa(a, b))
