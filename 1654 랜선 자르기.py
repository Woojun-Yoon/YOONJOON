# 이분 탐색
from sys import stdin
input = stdin.readline

def max_cut(num):
    cache = 0
    for i in range(k):
        cache += k_list[i] // num
    return cache >= n

k, n = map(int, input().split())
k_list = []
for _ in range(k):
    k_list.append(int(input()))

start = 1
end = (2 ** 31) - 1
while start < end:
    mid = (start + end + 1) // 2
    if max_cut(mid):
        start = mid
    else:
        end = mid - 1
print(int(start))