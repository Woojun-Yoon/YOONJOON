from sys import stdin
input = stdin.readline

div_num = int(input())
div_list = list(map(int, input().split()))
if div_num == 1:
    print(div_list[0] ** 2)
else:
    print(max(div_list) * min(div_list))