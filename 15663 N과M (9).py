from sys import stdin
from itertools import permutations
input = stdin.readline

n, m = map(int, input().split())
nums = sorted((map(int, input().split())))
nums = sorted(list(set(permutations(nums, m))))

for i in nums:
    print(*i)