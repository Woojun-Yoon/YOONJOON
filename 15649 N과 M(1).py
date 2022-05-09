from sys import stdin
from itertools import permutations
input = stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
# join and map으로 60ms 시간 단축 가능
for cache in permutations(nums, m):
    print(*cache) # unpacking 보다 join이 더 빠름