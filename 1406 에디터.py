from sys import stdin
from collections import deque
input = stdin.readline

word = deque(input().rstrip()) # 덱을 이용한 구현
word_len = len(word)
m = int(input())
curser = word_len
for _ in range(m):
    command = input().split()
    if command[0] == 'L':
        if curser == 0:
            continue
        else:
            curser -= 1
            word.appendleft(word.pop())
    elif command[0] == 'D':
        if curser == word_len:
            continue
        else:
            curser += 1
            word.append(word.popleft())
    elif command[0] == 'B':
        if curser == 0:
            continue
        else:
            word_len -= 1
            curser -= 1
            word.pop()
    elif command[0] == 'P':
        word_len += 1
        curser += 1
        word.append(command[1])
    else:
        pass
if curser < word_len:
    for _ in range(word_len - curser):
        word.append(word.popleft())
print(''.join(word))

'''
# 덱이 아닌 빈 리스트를 이용한 방법(스택)
stk = list(input().strip())
stk_cache = []
n = int(input())
for line in stdin: # ^Z 입력될때 까지 for문 순회
    if line[0] == 'L':
        if stk:
            stk_cache.append(stk.pop())
        else:
            continue
    elif line[0] == 'D':
        if stk_cache:
            stk.append(stk_cache.pop())
        else:
            continue
    elif line[0] == 'B':
        if stk:
            stk.pop()
        else:
            continue
    elif line[0] == 'P':
        stk.append(line[1])
print(''.join(stk + list(reversed(stk_cache))))
'''
