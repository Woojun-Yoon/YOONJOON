# 큐, 덱
from sys import stdin
from collections import deque
input = stdin.readline

cards = deque([i for i in range(1,int(input()) + 1)])
for _ in range(len(cards) - 1):
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)