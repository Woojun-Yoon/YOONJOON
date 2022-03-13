# 브루트포스 알고리즘

from sys import stdin
input = stdin.readline

def han_su_search(n):
    if 0 < n <= 99:
        return 1
    elif 100 <= n <= 999:
        cache_list = str(n)
        a1 = int(cache_list[0]) - int(cache_list[1])
        a2 = int(cache_list[1]) - int(cache_list[2])
        if a1 == a2:
            return 1
        else:
            return 0
    else:
        return 0

han_su = []
han_su_cache = []

for i in range(1,1001,1):
    result = han_su_search(i)
    if result:
        han_su.append(i)

n = int(input())

for j in range(len(han_su)):
    if han_su[j] <= n:
        han_su_cache.append(han_su[j])

print(len(han_su_cache))