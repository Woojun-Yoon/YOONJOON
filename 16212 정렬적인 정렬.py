from sys import stdin
input = stdin.readline

input()
nums = list(map(int, input().split()))
nums.sort()
print(*nums)