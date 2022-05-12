from sys import stdin
input = stdin.readline

dic = {}
n, m = map(int, input().split())
for _ in range(n):
    key, value = input().split()
    dic[key] = value

for _ in range(m):
    key = input().rstrip()
    print(dic.get(key))