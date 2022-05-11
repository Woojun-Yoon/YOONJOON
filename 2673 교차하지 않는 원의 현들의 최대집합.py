from sys import stdin
from itertools import combinations, permutations
input = stdin.readline

line = []
result = 0
count = 0
count_result = 0
n = int(input())
graph = [[] for _ in range(n)]
back = []
for _ in range(n):
    num1, num2 = map(int, input().split())
    # [small, big]
    if num1 < num2:
        line.append([num1, num2])
    else:
        line.append([num2, num1])
'''
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
'''
# 정리
def check(line1, line2): # line1 기준
    if (line1[0] < line2[0] and line1[1] > line2[1]) or (line1[0] > line2[0] and line1[1] < line2[1]):  return 1
    elif (line1[1] < line2[0]) or  (line2[1] < line1[0]):  return 1
    else:   return 0

for case in combinations(range(len(line)), 2):
    if check(line[case[0]], line[case[1]]):
        graph[case[0]].append(case[1])
        graph[case[1]].append(case[0])

def back_tracking(back, num):
    max_count = 0
    for 





    if len(back) == 0:
        return count



print(graph)

'''
for case in permutations(range(len(line)), 2):
    count += 1
    if check(line[case[0]], line[case[1]]):
        count_result += 1
    
    if count == n - 1:
        count = 0
        if result < count_result:
            result = count_result
        count_result = 0
'''