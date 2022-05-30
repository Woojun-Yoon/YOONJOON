from sys import stdin
input = stdin.readline

n = int(input())
cache1 = 0
cache2 = 1
result = 0
for _ in range(n - 1):
    result = cache1 + cache2
    cache1 = cache2
    cache2 = result

if n == 1:
    print(1)
else:   
    print(result)