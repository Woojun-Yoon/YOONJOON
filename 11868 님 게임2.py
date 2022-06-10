from sys import stdin
from functools import reduce
input = stdin.readline
# Sprague-Grundy Theorem
n = int(input())
grundy_num = reduce(lambda x, y : x ^ y, list(map(int, input().split())))
print('koosaga' if grundy_num else 'cubelover')