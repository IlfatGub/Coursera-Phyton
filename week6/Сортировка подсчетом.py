def CountSort(A):
    t = [0]*101

    for i in A:
        t[i] += 1

    A = []

    for i in range(101):
        A += [i]*t[i]
    return A

A = input().split()
print (CountSort(A))
