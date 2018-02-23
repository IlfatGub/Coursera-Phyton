H = int(input())
A = int(input())
B = int(input())
print((H // (A - B) - (A - (H % (A - B))) // (A - B)) + 1)
