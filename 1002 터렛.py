from math import sqrt
from sys import stdin
input = stdin.readline

T = int(input()) #테스트 개수 T

i = 0
while i < T: #마지막에 i++
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    h = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if h == 0: #두 점의 좌표가 같을 때
        if r1 == r2:
            print('-1')
        else:
            print('0')
    else: #두 점의 좌표가 다를 때
        if (r1 > r2+h) or (r2 > r1+h) or (r1+r2 < h):
            print('0')
        elif (r1 == r2+h) or (r2 == r1+h) or (r1+r2 == h):
            print('1')
        elif (r1 < r2+h) and (r2 < r1+h) and (r1+r2 > h):
            print('2')
    i = i + 1