# if you know, you can do everything
from sys import stdin
from collections import deque
from itertools import permutations
from itertools import combinations
from collections import Counter
from bisect import bisect_left, bisect_right
from collections import defaultdict
from math import comb
from heapq import heapify

input = stdin.readline

n, *data = map(int, input().split()) # split()은 공백, 엔터, 탭으로 토큰화 default
print(data)