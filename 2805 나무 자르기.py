# 이진 탐색 (반례 끝까지 찾기(많은 테스트 케이스로 실행))
# counter로 중복값 연산을 줄일 수 있음(효과 큼)
from sys import stdin
from collections import Counter
input = stdin.readline

def binary(m, list_tree):
    start = 0
    end = max(list_tree) # end 값 최소화로 시간복잡도 줄이기(효과 적음)
    wood = Counter(list_tree).items()
    while start < end:
        result_cache = 0
        mid = (start + end) // 2
        for i, j in wood:
            if i > mid:
                result_cache += (i - mid) * j
        
        if result_cache >= m:
            start = mid + 1
        else:
            end = mid 

    return end

n, m = map(int, input().split())
list_tree = list(map(int, input().split()))
result = binary(m, list_tree)
print(result - 1)