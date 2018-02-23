a = int(input())
b = int(input())
x = (1 // (a % b + 1) + 1) % 2
y = 1 // (a % b + 1)
print('NO' * x + 'YES' * y)
