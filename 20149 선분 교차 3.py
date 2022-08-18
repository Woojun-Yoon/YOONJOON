from sys import stdin
from typing import Sequence
input = stdin.readline

def ccw(p1 : Sequence[int], p2 : Sequence[int], p3 : Sequence[int]) -> int:
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def cross(p1 : Sequence[int], p2 : Sequence[int], p3 : Sequence[int], p4 : Sequence[int]):
    x1, x2 = p1[0] - p2[0], p3[0] - p4[0]
    y1, y2 = p1[1] - p2[1], p3[1] - p4[1]
    form1 = p1[0] * p2[1] - p1[1] * p2[0]
    form2 = p3[0] * p4[1] - p3[1] * p4[0]
    x = (form1 * x2 - form2 * x1) / (x1 * y2 - x2 * y1)
    y = (form1 * y2 - form2 * y1) / (x1 * y2 - x2 * y1)
    return x, y

if __name__ == '__main__':
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    a, b, c, d = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

    if ccw(a, b, c) * ccw(a, b, d) == 0 and ccw(c, d, a) * ccw(c, d, b) == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        if b >= c and a <= d:
            print("1") # NOT CROSS
            try:
                x, y = cross(a, b, c, d)
                print(x, y)
            except:
                if a > b:
                    a, b = b, a
                if c > d:
                    c, d = d, c
                if b == c:
                    print(b[0], b[1])
                elif a == d:
                    print(a[0], a[1])
        else:
            print("0")
    elif ccw(a, b, c) * ccw(a, b, d) <= 0 and ccw(c, d, a) * ccw(c, d, b) <= 0: # 선분 기준 타 두 점의 위치 파악을 하기위한 ccw값의 곱이 -1, 즉 서로 달라야함
        print("1")
        x, y = cross(a, b, c, d)
        print(x, y)
    else:
        print("0")