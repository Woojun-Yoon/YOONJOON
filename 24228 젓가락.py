from sys import stdin
input = stdin.readline

n, r = map(int, input().split())
print(n + (2 * r) - 1)