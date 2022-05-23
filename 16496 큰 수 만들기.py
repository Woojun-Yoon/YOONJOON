from sys import stdin
input = stdin.readline

n = int(input())
nums = list(input().rstrip().split())

for i in range(n - 1):
    index = i
    for j in range(i + 1, n):
        if int(nums[j] + nums[index]) > int(nums[index] + nums[j]):
            index = j
    nums[index], nums[i] = nums[i], nums[index]

result = ''.join(nums)
if nums.count('0') == n:
    result = '0'

print(result)