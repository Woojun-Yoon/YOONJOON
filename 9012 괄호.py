# 덱을 이용한 풀이
from sys import stdin
input = stdin.readline
from collections import deque
''' # ((()))(())((())) 잘못된 풀이!
for _ in range(int(input())):
    bracket = deque(input().strip())
    
    while len(bracket) > 2:
        if bracket[1] == '(' and bracket[2] == ')':
            cache = bracket.popleft()
            bracket.popleft()
            bracket.popleft()
            bracket.appendleft(cache)
        elif bracket[-3] == '(' and bracket[-2] == ')':
            cache = bracket.pop()
            bracket.pop()
            bracket.pop()
            bracket.append(cache)
        elif bracket[0] == '(' and bracket[1] == ')':
            bracket.popleft()
            bracket.popleft()
        elif bracket[-2] == '(' and bracket[-1] == ')':
            bracket.pop()
            bracket.pop()
        elif bracket[0] == '(' and bracket[-1] == ')':
            bracket.popleft()
            bracket.pop()
        else:
            break

    if len(bracket) == 2 and (bracket[0] == '(' and bracket[1] == ')'):
        print("YES")
    else:
        print("NO")
'''
'''
# 카운팅을 이용한 풀이
for _ in range(int(input())):
    bracket = input().strip()
    cache = 0
    for i in bracket:
        if i == '(':
            cache += 1
        elif i == ')':
            cache -= 1
        
        if cache < 0:
            print('NO')
            break
    
    if cache > 0:
        print("NO")
    elif cache == 0:
        print('YES')
'''
# 스택을 이용한 풀이
for _ in range(int(input())):
    bracket = input().strip()
    cache = []
    for i in bracket:
        if i == '(':
            cache.append(i)
        else:
            if len(cache) == 0:
                cache = [-1]
                break
            else:
                cache.pop()
    if len(cache) == 0:
        print("YES")
    else:
        print("NO")        

