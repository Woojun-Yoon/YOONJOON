# DP
# 그리디 알고리즘
from sys import stdin
input = stdin.readline
'''
n = int(input())
result = -1
for x in range(0,(n//5) + 1,1):
    for y in range(0,(n//3) + 1,1):
        if (x * 5 + y * 3) == n:
            result = x + y
print(result)
'''
'''
#DP 풀이
n = int(input())

dp = [-1] * 5001
dp[3] = dp[5] = 1

for i in range(6, n + 1):
    if i % 5 == 0:
        dp[i] = dp[i - 5] + 1
    elif i % 3 == 0:
        dp[i] = dp[i - 3] + 1
    elif dp[i - 3] > 0 and dp[i - 5] > 0:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
print(dp[n])
'''
#그리디 풀이

n = int(input())
result = 0

while n > 0:
    if n % 5 == 0:
        result += n // 5
        n = 0
        break
    else:
        n -= 3
        result += 1
if n:
    print(-1)
else:
    print(result)