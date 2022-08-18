'''
from sys import stdin
from collections import deque
input = stdin.readline

def spin(sel, way):
    rotate = [False, False, False, False]
    rotate[sel] = True
    for _ in range(sel - 1, -1, -1): # left
        if wheel[_][2] != wheel[_ + 1][-2]:
            rotate[_] = True
        else:
            break
    
    for _ in range(sel + 1, 4): # right
        if wheel[_][-2] != wheel[_ - 1][2]:
            rotate[_] = True
        else:
            break
    
    for _ in range(4):
        if rotate[_] and (way - _) % 2 == 0:
            wheel[_].rotate(-1)
        elif rotate[_] and (way - _) % 2 == 1:
            wheel[_].rotate(1)
    

if __name__ == '__main__':
    w1 = deque([*map(int, input().rstrip())])
    w2 = deque([*map(int, input().rstrip())])
    w3 = deque([*map(int, input().rstrip())])
    w4 = deque([*map(int, input().rstrip())])

    wheel = [w1, w2, w3, w4]

    for _ in range(int(input())):
        sel, way = map(int, input().split())
        if way == 1:
            spin(sel - 1, True)
        else:
            spin(sel - 1, False)
    
    result = 0
    for _ in range(4):
        result += wheel[_][0] * (2 ** _)
    
    print(result)
'''
from collections import deque
chain = [deque(list(input())) for _ in range(4)]
k = int(input())

def left(now, l, dir):
    if l < 0:
        return
    if chain[now][6] != chain[l][2]:
        left(l, l-1, -dir)
        chain[l].rotate(-dir)

def right(now, r, dir):
    if r > 3:
        return
    if chain[now][2] != chain[r][6]:
        right(r, r+1, -dir)
        chain[r].rotate(-dir)

for _ in range(k):
    num, dir = map(int, input().split())
    left(num-1, num-2, dir)
    right(num-1, num, dir)
    chain[num-1].rotate(dir)

answer = 0
for i in range(4):
    if chain[i][0] == "1":
        answer += (2**i)

print(answer)