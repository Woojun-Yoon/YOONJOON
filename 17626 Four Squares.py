from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    dp = [0, 1]

    for i in range(2, n + 1):
        check = 1e9
        j = 1
        while (j ** 2 <= i):
            check = min(check, dp[i - (j ** 2)])
            j += 1
        dp.append(check + 1)
    print(dp[n])