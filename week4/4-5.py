# Проверка числа на простоту
def IsPrime(n):
   d = 2
   while n % d != 0:
       d += 1
   if d == n:
       return True
   else:
       return False

def val(n):
    if IsPrime(n):
        return "YES"
    else:
        return "NO"

n = int(input())
print(val(n))