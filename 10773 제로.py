# 스택
from sys import stdin
input = stdin.readline
'''
num_list = []
k = int(input())
for _ in range(k):
    n = int(input())
    if n:
        num_list.append(n)
    else:
        del num_list[-1]
print(sum(num_list))
'''

input()
list = []
for i in map(int, stdin): #^z 입력시 종료(EOF 입력)
    list.append(i) if i else list.pop()
print(sum(list))