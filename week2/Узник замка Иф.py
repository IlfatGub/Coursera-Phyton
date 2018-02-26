a = int(input())
b = int(input())
q = int(input())
d = int(input())
e = int(input())
if a <= d and b <= e or a <= e and b <= d:
    print("YES")
elif q <= d and b <= e or q <= e and b <= d:
    print("YES")
elif q <= d and a <= e or q <= e and a <= d:
    print("YES")
else:
    print("NO")
