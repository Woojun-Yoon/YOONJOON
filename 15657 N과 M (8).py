from sys import stdin
from itertools import combinations_with_replacement
input = stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
nums = list(combinations_with_replacement(nums, m))

for _ in nums:
    print(*_)