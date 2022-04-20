from sys import stdin
input = stdin.readline

n = int(input())
for i in range(1, n + 1):
    print('*' * i, sep = '', end = '\n')
for j in range(n - 1, 0, -1):
    print('*' * j, sep = '', end = '\n')