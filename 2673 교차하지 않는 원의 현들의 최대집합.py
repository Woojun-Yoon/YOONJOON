import itertools
from sys import stdin
from itertools import permutations
input = stdin.readline

line = []
n = int(input())
for _ in range(n):
    num1, num2 = map(int, input().split())
    # [small, big]
    if num1 < num2:
        line.append([num1, num2])
    else:
        line.append([num2, num1])

def check(line1, line2): # line1 기준
    if line2[0] > line1[0] and line2[0] < line1[1]:
        if line2[1] < line1[1]:   return 1
        else:   return 0
    elif line1[0] > line2[0] and line1[0] > line2[1]:
        if line2[1] > line1[1]:   return 1
        elif line2[1] < line1[0]:   return 1
        else:   return 0
    elif line2[0] > line1[0] and line2[0] > line1[1]:
        return 1
    elif line2[0] < line1[0]:
        if line2[1] < line1[0]:   return 1
        elif line2[1] > line1[1] :   return 1
        else:   return 0
    else:
        return 0

# print(check(line[0], line[1]))
for case in permutations(line, 2):
    print(case[0], '&', case[1], bool(check(case[0], case[1])))

result = 0


# small -> big
'''
for num in range(n):
    if line[num][0] > line[num][1]:
        

    else:
'''
# [5, 27] & [1, 45] False
# [43, 72] & [31, 97] False
