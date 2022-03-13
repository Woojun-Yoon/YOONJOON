# 계수 정렬(같은 수가 자주 반복되는 리스트를 정렬할때 효과적)
from sys import stdin
input = stdin.readline

n = int(input()) # 수의 개수(1 <= n <= 10,000,000)
counting_sort = [0] * (10000 + 1) # 메모리 신경 쓰기 (int형 1000개가 4kb)
for _ in range(n): # n개의 수가 담긴 리스트
    counting_sort[int(input())] += 1


for i in range(10001):
    if counting_sort[i] > 0:
        while counting_sort[i] > 1000:
            print((str(i) + '\n') * 1000, end = '')
            counting_sort[i] -= 1000
        print((str(i) + '\n') * counting_sort[i], end = '')