# 재귀 함수
from sys import stdin
input = stdin.readline

def fac(n):
    if n == 0:
        return 1
    elif n == 0:
        return 1
    return n * fac(n - 1)
        
n = int(input())
print(fac(n))