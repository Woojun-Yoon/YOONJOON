from sys import stdin
input = stdin.readline

dp = [0] * 110
dp[0] = 1
dp[1] = 1
dp[2] = 1
for i in range(100):
    dp[i + 3] = dp[i] + dp[i + 1]

for _ in range(int(input())):
    print(dp[int(input())-1])
