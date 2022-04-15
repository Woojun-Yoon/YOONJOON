from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
c = list(map(int, input().split()))
d = a * b
for i in range(5):
    print(c[i] - d, end = ' ')