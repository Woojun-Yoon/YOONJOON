from sys import stdin
input = stdin.readline

n = int(input())
x_y = list(list(map(int, input().split())) for _ in range(n))
sort_x = sorted(x_y, key = lambda x: x[0])
sort_y = sorted(sort_x, key = lambda x: x[1])
for i in range(n):
    print(*sort_y[i])
