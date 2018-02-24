# Узник замка Иф
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if (d * e >= a * b) or (d * e >= c * b) or (d * e >= a * c):
    print("YES")
else:
    print("NO")
