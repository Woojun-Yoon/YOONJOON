from sys import stdin
input = stdin.readline

poketmon_name = {}
poketmon_num = {}
n ,m = map(int, input().split())

for num in range(1, n + 1):
    cache = input().rstrip()
    poketmon_name[cache] = num
    poketmon_num[num] = cache

for _ in range(m):
    cache = input()
    try:
        print(poketmon_num.get(int(cache)))
    except:
       pass
    try:
        print(poketmon_name[cache.rstrip()])
    except:
       pass