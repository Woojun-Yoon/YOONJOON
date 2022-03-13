from sys import stdin
input = stdin.readline

dot_list = []
for _ in range(int(input())):
    dot_list.append(list(map(int, input().split())))
dot_list.sort()
for i in range(len(dot_list)):
    print(*dot_list[i])