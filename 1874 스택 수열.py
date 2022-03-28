from sys import stdin
input = stdin.readline

n = int(input())
count = 0
num_list = [i for i in range(n, 0 , -1)]
want_list = []
make_list = []
stack = []
result = []
for _ in range(n):
    want_list.append(int(input()))

while True:
    if len(make_list) == n:
        break

    if stack and stack[-1] == want_list[count]:
        make_list.append(stack.pop())
        result.append("-")
        count += 1       
    elif num_list and num_list[-1] != want_list[count]:
        stack.append(num_list.pop())
        result.append("+")
    elif num_list and num_list[-1] == want_list[count]:
        make_list.append(num_list.pop())
        result.append("+")
        result.append("-")
        count += 1
    else:
        break

if len(make_list) == n:
    print('\n'.join(result))
else:
    print("NO")