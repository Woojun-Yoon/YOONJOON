from sys import stdin
from math import sqrt, pi, acos, sin
input = stdin.readline

if __name__ == '__main__':
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    result = 0
    # 두 원의 중심 간의 거리
    l = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # 두 원이 만나지 않는 경우
    if l >= r1 + r2:
        result = 0
    # 두 원이 만나 교차하는 영역이 있는 경우
    else:
        # 원1이 내부에 있는 경우
        if l <= abs(r1 - r2) and r1 <= r2:
            result = pi * r1 * r1
        # 원2가 내부에 있는 경우
        elif l <= abs(r1 - r2) and r1 > r2:
            result = pi * r2 * r2
        # 두 점에서 만나는 경우
        else:
            theta1 = acos((r1 ** 2 + l ** 2 - r2 ** 2) / (2 * r1 * l)) * 2
            theta2 = acos((r2 ** 2 + l ** 2 - r1 ** 2) / (2 * r2 * l)) * 2

            area1 = 0.5 * r1 * r1 * (theta1 - sin(theta1))
            area2 = 0.5 * r2 * r2 * (theta2 - sin(theta2))
            result = area1 + area2
    
    print('%.3f' % result)



