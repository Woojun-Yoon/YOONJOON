from sys import stdin
input = stdin.readline
from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = set([])
for _ in combinations_with_replacement(nums, m):
    if _ not in result:
        result.add(_)
        print(' '.join(map(str, _)))

