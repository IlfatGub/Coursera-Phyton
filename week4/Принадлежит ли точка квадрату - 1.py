# Принадлежит ли точка квадрату - 1
def square(x, y):
    if -1 <= x <= 1 and-1 <= y <= 1:
        return True
    else:
        return False


def IsPointSquare(x, y):
    return square(x, y)

x = float(input())
y = float(input())
if IsPointSquare(x, y):
    print("YES")
else:
    print("NO")
