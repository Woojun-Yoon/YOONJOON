from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
n = int(input())
cache1 = abs(a - b)
cache2 = 1001
for _ in range(n):
    cache = abs(int(input()) - b)
    if cache2 > cache:
        cache2 = cache

if cache1 <= cache2:
    print(cache1)
else:
    print(cache2 + 1)