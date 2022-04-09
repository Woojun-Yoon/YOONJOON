from sys import stdin
input = stdin.readline

nums = list(map(int, input().rstrip()))
print(*sorted(nums, reverse = 1), sep = '')