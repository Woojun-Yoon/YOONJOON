from sys import stdin
from collections import deque
input = stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = deque([*map(int, input().split())])
    robot = deque([0] * n)
    result = 0

    while True:
        # 1
        a.rotate(1)
        robot.rotate(1)
        robot[-1] = 0
        # 2
        for _ in range(n - 2, -1, -1):
            if robot[_] == 1:
                if robot[_ + 1] == 0 and a[_ + 1] > 0:
                    robot[_] = 0
                    robot[_ + 1] = 1
                    a[_ + 1] -= 1
            if robot[-1] == 1:
                robot[-1] = 0
        # 3
        if a[0] > 0 and robot[0] == 0:
            a[0] -= 1
            robot[0] = 1
        result += 1
        # 4
        if a.count(0) >= k:
            break
    
    print(result)