from sys import stdin
input = stdin.readline

while True:
    words = list(input().rstrip())
    if words[0] == '.':
        break
    
    stack = []
    Q = True
    for i in range(len(words)):
        if words[i] == '(':
            stack.append('(')
        elif words[i] == '[':
            stack.append('[')
        elif words[i] == ')':
            if len(stack) != 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    Q = False
                    break
            else:
                Q = False
                break
        elif words[i] == ']':
            if len(stack) != 0:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    Q = False
                    break
            else:
                Q = False
                break
        else:
            continue
    if Q and len(stack) == 0:
        print("yes")
    else:
        print("no")