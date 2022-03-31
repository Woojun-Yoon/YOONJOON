from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    card = input().split()
    result = deque([card[0]])
    for i in range(1, n):
        if card[i] <= result[0]:
            result.appendleft(card[i])
        else:
            result.append(card[i])
    print(*result, sep = '')