# if you know, you can do everything
# git 강제 push command : git push -u origin +master
from sys import stdin
from collections import deque
# deque은 무작위 접근시 시간복잡도가 O(n), i번째 데이터에 접근하려면 앞/뒤로 i번 순회 해야하기 때문
# 큐와 덱은 pop, append가 O(1)이며, 단점또한 동일 따라서, 큐쓸때도 그냥 덱쓰면 됨
from itertools import permutations
from itertools import combinations
from collections import Counter
from bisect import bisect_left, bisect_right
from collections import defaultdict
from math import comb, ceil, log2
from heapq import heapify
from copy import deepcopy
from decimal import *
from typing import List # 알아볼 필요가 있음
# deepcopy는 아예 완벽하게 복사해 버려서, 서로 영향을 안받음(가르키는 메모리 주소가 다름)
from cmath import *

input = stdin.readline
'''
n, *data = map(int, input().split()) # split()은 공백, 엔터, 탭으로 토큰화 default
print(data)
'''
'''
command = input().split()
command = deque(command)
print(command.index("123"))
'''
'''
for i in range(10,-1,-1):
    print(i)
'''
'''
getcontext().prec = 500
getcontext().rounding = ROUND_HALF_UP # 사사오입
print(Decimal(1 / 3))
print(Decimal('1')/ Decimal('3'))
'''
'''
print(int(ceil(log2(5))))
for i in range(int(input())):
    i = (i & -i)
    print(i)
'''
# 고속푸리에변환 구현

def fft(p):
    n = len(p)
    if n == 1:
        return p
    p_even = fft(p[0::2])
    p_odd = fft(p[1::2])
    w = [exp(2j * pi * x / n) for x in range(n // 2)]
    return [p_even[x] + w[x] * p_odd[x] for x in range(n // 2)] + [p_even[x] - w[x] * p_odd[x] for x in range(n // 2)]

def ifft(p):
    n = len(p)
    if n == 1:
        return p
    p_even = fft(p[0::2])
    p_odd = fft(p[1::2])
    w = [exp(-2j * pi * x / n) for x in range(n // 2)]
    return [p_even[x] + w[x] * p_odd[x] for x in range(n // 2)] + [p_even[x] - w[x] * p_odd[x] for x in range(n // 2)]

for _ in range(5, -1, -1):
    print(_)

x = 5
if x > 0:
    print(1)
elif x > 1:
    print(2)
else:
    print(3)