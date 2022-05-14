from sys import stdin
input = stdin.readline

cham = int(input())
way = []
for _ in range(6):
    a, b = map(int, input().split())
    way.append(b)

long = 0
short = 0

for i in range(6):
    cache = way[i] * way[(i + 1) % 6]
    if long < cache:
        long = cache
        cache_idx = i

short = way[(cache_idx + 3) % 6] * way[(cache_idx + 4) % 6]
print(cham * (long - short))
