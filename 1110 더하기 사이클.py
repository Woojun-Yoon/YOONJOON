from sys import stdin
input = stdin.readline

def plus_cycle(cache):
    cache_10 = cache // 10
    cache_1 = cache % 10
    cache_plus = cache_10 + cache_1
    if cache_plus < 10:
        cache = (cache_1 * 10) + cache_plus
        return cache
    else:
        cache_plus_R = cache_plus % 10
        cache = (cache_1 * 10) + cache_plus_R
        return cache

n = int(input())
cache = 0
cycle = 0

if 0 < n < 10:
    cache = (10 * n) + n
    cycle += 1
else:
    cache = n

while True:
    cache = plus_cycle(cache)
    if cache == n:
        cycle += 1
        print(cycle)
        break
    else:
        cycle += 1