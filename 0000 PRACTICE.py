from sys import stdin
from collections import deque
from itertools import permutations
from collections import Counter
from bisect import bisect_left, bisect_right
input = stdin.readline

n, *data = map(int, input().split()) # split()은 공백, 엔터, 탭으로 토큰화 default
print(data)