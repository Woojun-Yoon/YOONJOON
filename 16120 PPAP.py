from sys import stdin
input = stdin.readline

words = list(input().rstrip())
stack = []

for word in words:
    stack.append(word)

    if len(stack) >= 4:
        if stack[-4] == 'P' and stack[-3] == 'P' and stack[-2] == 'A' and stack[-1] == 'P':
            stack.pop()
            stack.pop()
            stack.pop()


if stack == ['P'] or stack == ['P','P','A','P']:
    print("PPAP")
else:
    print("NP")