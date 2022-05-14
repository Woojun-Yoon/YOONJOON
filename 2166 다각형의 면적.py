from sys import stdin
input = stdin.readline

n = int(input())
num1 = list(map(int, input().split()))
nums = [num1]
for _ in range(n - 1):
    nums.append(list(map(int, input().split())))
nums.append(num1)
left = 0
right = 0
for i in range(n):
    left += nums[i][0] * nums[i + 1][1]
for i in range(n):
    right += nums[i][1] * nums[i + 1][0]

print(0.5 * abs(left - right))