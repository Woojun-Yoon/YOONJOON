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
from math import comb
from heapq import heapify
from copy import deepcopy
from decimal import *
# deepcopy는 아예 완벽하게 복사해 버려서, 서로 영향을 안받음(가르키는 메모리 주소가 다름)

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
for i in range(10,-1,-1):
    print(i)

getcontext().prec = 500
getcontext().rounding = ROUND_HALF_UP # 사사오입
print(Decimal(1 / 3))
print(Decimal('1')/ Decimal('3'))
