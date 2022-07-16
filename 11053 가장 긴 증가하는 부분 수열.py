from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = [*map(int, input().split())]

    dp = [0] * (n + 1)

    for i in range(n):
        for j in range(n):
            if nums[i] > nums[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1

    print(max(dp))