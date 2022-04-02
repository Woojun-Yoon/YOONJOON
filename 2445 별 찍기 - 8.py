from sys import stdin
input = stdin.readline

n = int(input())
for i in range(1, n, 1):
    print('*' * i, ' ' * (2 * (n - i)),'*' * i, sep = '')
for i in range(n , 0, -1):
    print('*' * i, ' ' * (2 * (n - i)),'*' * i, sep = '')