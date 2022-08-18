from sys import stdin
from itertools import combinations
input = stdin.readline


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        p = [0 for _ in range(N)]
        xtotal, ytotal = 0, 0
        for _ in range(N):
            x, y = map(int, input().split())
            xtotal += x
            ytotal += y
            p[_] = [x, y]
        
        _max = 1000000
        comb = list(combinations(range(N), N // 2))
        for com in comb[:len(comb) // 2]:
            x, y = 0, 0
            for c in com:
                x += p[c][0]
                y += p[c][1]
            x -= xtotal - x
            y -= ytotal - y

            scala = (x ** 2 + y ** 2) ** 0.5
            if _max > scala:
                _max = scala
        print(_max)
