from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    g = []
    b = []
    for _ in range(n):
        heappush(g, [*map(int, input().split())])
    for _ in range(k):
        b.append(int(input()))
    b.sort()

    result = 0
    cache = []

    for bag in b:
        while g and bag >= g[0][0]: # gem이 있고, bag에 gem을 담을 수 있는 경우
            heappush(cache, -heappop(g)[1]) # heap sort
        if cache:
            result -= heappop(cache)
        elif not g:
            break
    print(result)