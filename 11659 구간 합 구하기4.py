from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * (n + 1)

for a in range(n):
    dp[a + 1] = dp[a] + nums[a]

for b in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])