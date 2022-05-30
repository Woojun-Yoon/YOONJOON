from sys import stdin
input = stdin.readline

nums = list(map(int, input().split(',')))
print(sum(nums))