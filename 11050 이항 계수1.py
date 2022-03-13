from sys import stdin
input = stdin.readline

def fac(n):
    if n == 0:
        return 1
    elif n == 0:
        return 1
    return n * fac(n - 1)

n, k = map(int, input().split())

result = (fac(n) // fac(k)) // fac(n - k)
print(result)