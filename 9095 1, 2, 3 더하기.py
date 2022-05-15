from sys import stdin
input = stdin.readline

dp = [0] * 12
dp[0] = 1
dp[1] = 2
dp[2] = 4
dp[3] = 7
for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for _ in range(int(input())):
    print(dp[int(input()) - 1])