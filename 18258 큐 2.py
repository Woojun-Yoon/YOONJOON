from sys import stdin
from collections import deque
input = stdin.readline

q = deque([])

for _ in range(int(input())):
    com = input().split()

    if com[0] == "push":
        q.appendleft(com[1])
    elif com[0] == "pop":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif com[0] == "size":
        print(len(q))
    elif com[0] == "front":
        if q:
            print(q[-1])
        else:
            print(-1)
    elif com[0] == "back":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(0)
        else:
            print(1)