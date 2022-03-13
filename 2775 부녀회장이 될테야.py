from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    cache_list = []
    for i in range(k+1):
        cache_list.append([])
    for j in range(n):
        cache_list[0].append(j + 1)
    for x in range(1,k+1):
        for y in range(n):
            cache_list[x].append(sum(cache_list[x-1][:y+1]))
    print(cache_list[k][n-1])