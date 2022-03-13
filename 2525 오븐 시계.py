from sys import stdin
input = stdin.readline

h, m = map(int, input().split())
c = int(input())
ch = c // 60 # 분단위로 주어진 c를 시간 단위로 바꿈
cm = c % 60
cache_h = 0
cache_m = 0

if (m + cm) >= 60:
    cache_h = h + ch + 1
    cache_m = m + cm - 60
else:
    cache_h = h + ch
    cache_m = m + cm

if cache_h >= 24:
    cache_h -= 24

print(cache_h,cache_m)
