# 덱
from sys import stdin
from collections import deque
input = stdin.readline

dq = deque([])
for _ in range(int(input())):
    com = input().split()
    if com[0] == 'push_front':
        dq.appendleft(com[1])
    elif com[0] == 'push_back':
        dq.append(com[1])
    elif com[0] == 'pop_front':
        if dq:  print(dq.popleft())
        else: print(-1)
    elif com[0] == 'pop_back':
        if dq:  print(dq.pop())
        else: print(-1)
    elif com[0] == 'size':
        print(len(dq))
    elif com[0] == 'empty':
        print(1 - int(bool(dq)))
    elif com[0] == 'front':
        if dq:  print(dq[0])
        else:   print(-1)
    elif com[0] == 'back':
        if dq:  print(dq[-1])
        else:   print(-1)
    else:
        pass