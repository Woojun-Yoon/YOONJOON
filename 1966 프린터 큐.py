from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    stack = []
    count = deque([i for i in range(n)])
    priority = deque(list(map(int, input().split())))
    while ((len(stack)) < n):
        max_cache = max(priority)
        if max_cache == priority[0]: # 맨 왼쪽 인덱스가 max와 값이 같은 경우
            priority.popleft()
            stack.append(count.popleft())
        else: # 맨 왼쪽 인덱스가 max와 값이 다른 경우
            priority.append(priority.popleft())
            count.append(count.popleft())
    print(stack.index(m) + 1)