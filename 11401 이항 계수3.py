from sys import stdin
from sys import exit
input = stdin.readline
limit = 1000000007
'''
n, k = map(int, input().split())
if n - k < k:
    k = n - k

if k == 0:
    print(1)
    quit()

top = n
bottom = 1
for i in range(1, k):
    top = top * (n - i) % limit
    bottom = bottom * (i + 1) % limit

print(top * pow(bottom, -1, limit) % limit)
'''
# 분할정복 거듭제곱 사용 1.1s 
def power(a, b):
    result = 1
    while(b > 0):
        if (b % 2) == 1:
            result = (result * a) % limit
        a = (a * a) % limit
        b = b // 2
    return result
# DP로 시간 단축? (int 범위 초과로 메모리 공간 부족)
def fac(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % limit
    return result

n, k = map(int, input().split())
if (k == 0) or (n == k):
    print(1)
    exit()

a, b, c = fac(n), fac(k), fac(n - k)
print(a * power(b * c, limit - 2) % limit)