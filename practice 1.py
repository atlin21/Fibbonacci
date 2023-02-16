def fibb(n):
    if n <= 2:
        return 1
    elif n > 2:
        return fibb(n - 1) + fibb(n - 2)
print("enter the term number: ")
n = int(input())
print(fibb(n))


