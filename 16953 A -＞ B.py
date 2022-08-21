from sys import stdin
from collections import deque
input = stdin.readline

if __name__ == '__main__':
    a, b = map(int, input().split())
    cache = deque()
    cache.append((a, 1))
    result = 0

    while(cache):
        x, y = cache.popleft()
        if x > b:
            continue
        if x == b:
            print(y)
            break
        cache.append((int(str(x) + '1'), y + 1))
        cache.append((x * 2, y + 1))
    else:
        print('-1')