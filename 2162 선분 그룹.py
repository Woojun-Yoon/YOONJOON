from sys import stdin
from typing import Sequence
input = stdin.readline

def ccw(p1 : Sequence[int], p2 : Sequence[int], p3 : Sequence[int]) -> int:
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def check(p1 : Sequence[int], p2 : Sequence[int]) -> int:
    a, b, c, d = [p1[0], p1[1]], [p1[2], p1[3]], [p2[0], p2[1]], [p2[2], p2[3]]
    if ccw(a, b, c) * ccw(a, b, d) == 0 and ccw(c, d, a) * ccw(c, d, b) == 0:
        if min(a[0], b[0]) <= max(c[0], d[0]) and min(c[0], d[0]) <= max(a[0], b[0]) and min(a[1], b[1]) <= max(c[1], d[1]) and min(c[1], d[1]) <= max(a[1], b[1]):
            return 1
    elif ccw(a, b, c) * ccw(a, b, d) <= 0 and ccw(c, d, a) * ccw(c, d, b) <= 0: # 선분 기준 타 두 점의 위치 파악을 하기위한 ccw값의 곱이 -1, 즉 서로 달라야함
        return 1
    return 0

def find(n):
    if nums[n] < 0:
        return n
    x = find(nums[n])
    nums[n] = x
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    
    if nums[x] < nums[y]:
        nums[x] += nums[y]
        nums[y] = x
    else:
        nums[y] += nums[x]
        nums[x] = y

if __name__ == '__main__':
    n = int(input())
    nums = [-1 for _ in range(n + 1)]
    points = []
    for _ in range(n):
        points.append([*map(int, input().split())])
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if check(points[i], points[j]):
                union(i + 1, j + 1)
    
    count = 0
    _max = 0
    for _ in nums[1:]:
        if _ < 0:
            count += 1
            _max = max(_max, abs(_))
    
    print(count)
    print(_max)
