objects = input().split()
o = set()
ans = 0
for obj in objects:
    if obj not in o:
        o.add(obj)
        ans += 1
print(ans)
