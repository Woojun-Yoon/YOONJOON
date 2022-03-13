from sys import stdin
from math import sqrt
input = stdin.readline
''' 시간 초과
while True:
    n = int(input())
    if n == 0:
        break
    a, b = n, 2 * n
    prime_list = [True for _ in range(b+1)]
    prime_list[0] = False; prime_list[1] = False

    for i in range(2, int(sqrt(b)) + 1):
        if prime_list[i]:
            j = 2
            while i * j <= b:
                prime_list[i * j] = False
                j += 1
    print(len([i for i in range(a+1, b+1) if prime_list[i]]))
'''
prime_list = [True for _ in range(246912+1)]
prime_list[0] = False; prime_list[1] = False

for i in range(2, int(sqrt(246912)) + 1):
    if prime_list[i]:
        j = 2
        while i * j <= 246912:
            prime_list[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(len([i for i in range(n + 1, 2 * n + 1) if prime_list[i]]))

