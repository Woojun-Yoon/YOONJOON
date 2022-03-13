# 재귀 함수
from sys import stdin
input = stdin.readline

def pibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pibo(n - 1) + pibo(n - 2)

n = int(input())
print(pibo(n))