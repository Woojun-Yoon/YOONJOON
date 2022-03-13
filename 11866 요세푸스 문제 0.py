# 요세푸스 순열
# 일반 점화식 풀이
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
num = list(range(1, n+1))
result = []
i = 0
while num:
    i = (i + m - 1) % len(num)
    result.append(str(num.pop(i)))
print('<',', '.join(result), '>', sep = '')