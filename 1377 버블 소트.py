from sys import stdin
input = stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append((int(input()), _))

sorted_nums = sorted(nums, key = lambda x : x[0])

result = 0
for _ in range(len(nums)):
    cache = sorted_nums[_][1] - nums[_][1]
    result = max(result, cache)

print(result + 1)