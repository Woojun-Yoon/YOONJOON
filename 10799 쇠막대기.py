from sys import stdin
input = stdin.readline

bra = input().rstrip()
stack = []
count = 1
result = 0
for item in bra:
    if item == '(':
        stack.append(item)
        count = 1
    else: # ')' 가 입력된 경우
        if (stack[-1] == '(') and count: # 레이져인 경우
            stack.pop()
            count = 0
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)