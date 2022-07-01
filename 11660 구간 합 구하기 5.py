from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    nums = [[*map(int, input().split())] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + nums[i][j]

    for _ in range(m):
        a1, a2, b1, b2 = map(int, input().split())
        print(dp[b1][b2] - (dp[a1 - 1][b2] + dp[b1][a2 - 1] - dp[a1 - 1][a2 - 1]))
        