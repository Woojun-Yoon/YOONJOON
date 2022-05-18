from sys import stdin
input = stdin.readline
from itertools import permutations
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for num in permutations(nums, m):
    print(*num)