from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    result = 0
    high = 0
    for num in range(len(nums) - 1, -1, -1):
        if nums[num] > high:
            high = nums[num]
        else:
            result += high - nums[num]
    print(result)