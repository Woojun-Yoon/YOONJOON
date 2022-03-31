from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    er = 0
    r_count = 0
    p = input().rstrip().replace('RR', '')
    n = int(input())
    array = input().rstrip()
    if len(array) > 2:
        array = deque(array[1:-1].split(','))
    else:
        array = []
    for com in p:
        if com == 'R': # R일때
            r_count += 1
        else: # D일때
            if array:
                if (r_count % 2) == 1:
                    array.pop()
                    continue
                else:
                    array.popleft()
            else:
                er = 1
                break
    if (r_count % 2) == 1:
        array.reverse()

    if er:
        print("error")
    else:
        print('[', end = '')
        print(','.join(array), end = '')
        print(']')