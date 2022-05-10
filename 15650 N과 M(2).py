from sys import stdin
from itertools import combinations
input = stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
for cache in combinations(nums, m):
    print(*cache)