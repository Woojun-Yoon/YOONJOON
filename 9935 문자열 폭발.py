from sys import stdin
input = stdin.readline

words = input().rstrip()
bomb = input().rstrip()
bomb_len = len(bomb)
stack = []

for item in words:
    stack.append(item)
    if item == bomb[-1] and ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")