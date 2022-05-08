from sys import stdin
input = stdin.readline

expression = input().rstrip()

stack = []
ans = ""
for s in expression:
    if s == '+' or s == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(s)
    elif s == '*' or s == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(s)
    elif s == '(':
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    else:
        ans += s

while stack: # 스택에 item이 남아있을때, 모두 pop하고 출력
    ans += stack.pop()

print(ans)