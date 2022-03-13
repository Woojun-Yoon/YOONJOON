# 브루트포스 알고리즘
from sys import stdin
input = stdin.readline

def maker(n): #n은 str
    cache = 0
    for i in range(len(n)):
        cache += int(n[i])
    return int(n) + cache

n = input().strip()
result = []
for i in range(int(n),1,-1):
    if maker(str(i)) == int(n):
        result.append(i)
if result:
    print(min(result))
else:
    print('0')