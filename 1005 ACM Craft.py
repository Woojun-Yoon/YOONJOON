#위상 정렬? DFS?
#DP -> cache 사용
from sys import stdin

def min_time(conTime, route, cache, W):
    time = 0
    for item in route[W-1]:
        if cache[item - 1] == -1:
            cache[item - 1] = min_time(conTime, route, cache, item)
            time = max(time, cache[item - 1])
        else:
            time = max(time, cache[item - 1])
    return conTime[W - 1] + time

T = int(stdin.readline())

for i in range(T): # 테스트 케이스에 대한 반복문
    N, K = map(int, stdin.readline().split()) # N = 건물의 개수, K = 건물간의 건설순서 규칙의 총 개수
    ConTime = list(map(int, stdin.readline().split())) #각 건물의 건설 소요 시간
    route = [[] for _ in range(N)] # 건물의 개수만큼 이중 리스트 생성(n번째 건물을 짓기위해 먼저 지어야 하는 건물번호를 추가)
    for _ in range(K):
        X, Y = map(int, stdin.readline().split()) # 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능
        route[Y-1].append(X)
    W = int(stdin.readline()) # W는 목표 건물
    cache = [-1] * N

    print(min_time(ConTime, route, cache, W))

    

    


    


