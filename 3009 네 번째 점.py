from sys import stdin
input = stdin.readline

x = []
for _ in range(3):
    x.append(list(map(int, input().split())))

result_list = []

for i in range(2):
    if x[0][i] == x[1][i]:
        result_list.append(x[2][i])
    elif x[1][i] == x[2][i]:
        result_list.append(x[0][i])
    else:
        result_list.append(x[1][i])

print(*result_list)