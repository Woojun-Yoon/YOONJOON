from sys import stdin
input = stdin.readline

n = int(input())
for i in range(n , 0, -1):
    print((n - i) * ' ' + (i * 2 - 1) * '*', sep = '')