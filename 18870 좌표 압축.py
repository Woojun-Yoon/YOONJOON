from sys import stdin
from bisect import bisect_left
input = stdin.readline
''' BISECTf를 이용한 이진탐색 풀이
n = int(input())
n_list = list(map(int, input().split()))
sort_list = sorted(set(n_list))
for i in range(n):
    print(bisect_left(sort_list, n_list[i]), end = ' ')
'''
# 딕셔너리를 이용한 풀이
n = int(input())
n_list = list(map(int, input().split()))
sort_list = sorted(set(n_list))
count_dict = {n:i for i, n in enumerate(sort_list)} # enumerate로 인덱스 값 튜플로 출력, i = index, n = velue reverse
print(" ".join(str(count_dict[num]) for num in n_list))