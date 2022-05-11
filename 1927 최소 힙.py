from sys import stdin
import heapq
input = stdin.readline

box = []
heapq.heapify(box)

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if len(box) == 0:
            print('0')
        else:
            print(heapq.heappop(box))
    else:
        heapq.heappush(box, num)
