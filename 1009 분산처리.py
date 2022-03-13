from sys import stdin
input = stdin.readline

cache = [[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1],[10]]

for _ in range(int(input())):
    a, b = map(int, input().split())
    a_cache = (a % 10) - 1
    b_cache = b % len(cache[a_cache])
    print(cache[int(a_cache)][b_cache - 1])
# 계산 과정에서 수가 커질경우 시간복잡도 생각하기