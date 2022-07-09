from sys import stdin
from typing import Sequence
input = stdin.readline

def ccw(p1 : Sequence[int], p2 : Sequence[int], p3 : Sequence[int]) -> int:
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


if __name__ == '__main__':
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    a, b, c, d = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

    if ccw(a, b, c) * ccw(a, b, d) < 0 and ccw(c, d, a) * ccw(c, d, b) < 0: # 선분 기준 타 두 점의 위치 파악을 하기위한 ccw값의 곱이 -1, 즉 서로 달라야함
        print("1")
    else:
        print("0")

