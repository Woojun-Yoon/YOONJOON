from sys import stdin
import heapq
input = stdin.readline

heap = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print('0')
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))