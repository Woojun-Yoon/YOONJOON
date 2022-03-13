# 스택
from sys import stdin
input = stdin.readline

stack_list = [] # 스택을 표현할 리스트
n = int(input()) # command 개수

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        stack_list.append(command[1])
    elif command[0] == 'pop':
        if stack_list:
            print(stack_list.pop(-1))
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(stack_list))
    elif command[0] == 'empty':
        print(1 - int(bool(stack_list)))
    elif command[0] == 'top':
        if stack_list:
            print(stack_list[-1])
        else:
            print('-1')
    else:
        pass