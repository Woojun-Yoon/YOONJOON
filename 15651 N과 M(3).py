from sys import stdin
from itertools import product
input = stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

print('\n'.join((map(' '.join, product(map(str, nums), repeat = m)))))

'''
for cache in product(nums, repeat = m):
    print(*cache)
'''