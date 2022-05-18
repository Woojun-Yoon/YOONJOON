from sys import stdin
from itertools import combinations
input = stdin.readline
# just use backtracking
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for num in combinations(nums, m):
    print(*num)