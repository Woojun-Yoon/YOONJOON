from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())
nums = Counter(list(map(int, input().split())))
print(nums[int(input())])