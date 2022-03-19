from sys import stdin
from bisect import bisect_left, bisect_right
from collections import Counter
input = stdin.readline


''' # bisect를 이용한 이분탐색 방법
n = int(input())
n_list = list(map(int, input().split()))
n_list = sorted(n_list)
m = int(input())
m_list = list(map(int, input().split()))
result_list = []
for i in range(m):
    print(bisect_right(n_list, m_list[i]) - bisect_left(n_list, m_list[i]), end = ' ')
'''
# Counter 를 이용한 dict 풀이

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

count = Counter(n_list)

for i in range(m):
    if m_list[i] in count:
        print(count[m_list[i]], end = ' ')
    else:
        print(0, end = ' ')