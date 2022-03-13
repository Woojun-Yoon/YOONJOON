from sys import stdin
from math import sqrt
input = stdin.readline

''' 오래 걸리지만 정답
n = int(input())
for i in range(2, n + 1, 1):
    while n % i == 0:
        print(i)
        n = n // i
'''

# 시간 단축

n = int(input())
for i in range(2, int(sqrt(n)) + 1):
    while n % i == 0:
        print(i)
        n //= i
if n > 1:
    print(n)


