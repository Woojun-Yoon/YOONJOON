from sys import stdin
input = stdin.readline

set_cache = set()

for _ in range(10):
    n = int(input())
    n = n % 42
    set_cache.add(n)

print(len(set_cache)) # set() 을 이용한 풀이