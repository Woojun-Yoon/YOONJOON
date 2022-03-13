# 큐
from sys import stdin
input = stdin.readline

Queue_list = [] # 큐를 표현할 리스트

n = int(input()) # command 개수

for _ in range(n):
    command = input().split() # list로 해서 실행시간 up
    if command[0] == 'push':
        Queue_list.append(command[1])
    elif command[0] == 'pop':
        if Queue_list:
            print(Queue_list.pop(0))
        else:
            print('-1')
    elif command[0] == 'front':
        if len(Queue_list):
            print(Queue_list[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if Queue_list:
            print(Queue_list[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(Queue_list))
    elif command[0] == 'empty':
        print(1 - int(bool(Queue_list)))
    else:
        pass