from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
print(abs(n - m))