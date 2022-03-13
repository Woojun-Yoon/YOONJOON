# 에라토스테네스의 체
from sys import stdin
from math import sqrt
input = stdin.readline
m, n = map(int, input().split())

prime_list = [True for _ in range(n+1)]
prime_list[0] = False; prime_list[1] = False

for i in range(2, int(sqrt(n)) + 1):
    if prime_list[i]:
        j = 2
        while i * j <= n:
            prime_list[i * j] = False
            j += 1

result_list = []
for i in range(m ,len(prime_list)):
    if prime_list[i] == True:
        result_list.append(i)
print(*result_list, sep='\n')

