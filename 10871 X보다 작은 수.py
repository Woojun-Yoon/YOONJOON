from sys import stdin
input = stdin.readline
cache = []
n, x = map(int, input().split()) #n은 정수의 갯수, x는 기준이 되는 정수
a = list(map(int, input().split()))
for i in range(n):
    if a[i] < x:
        cache.append(a[i])
print(*cache) # list cache unpacking

# print(a[i], end = ' ') 를 통한 풀이 가능
        

