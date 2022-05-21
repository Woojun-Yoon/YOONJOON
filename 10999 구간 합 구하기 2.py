from sys import stdin
input = stdin.readline
# 펜윅트리 2개 구현으로 풀기
def fen_sum(index):
    result1 = 0
    result2 = 0
    index_cache = index
    while index > 0:
        result1 += fen[index]
        result2 += fen_cache[index]
        index -= (index & -index)
    return result1 * index_cache + result2

def fen_update(index, cache1, cache2):
    while index < len(fen):
        fen[index] += cache1
        fen_cache[index] += cache2
        index += (index & -index)

def range_update(a, b, c):
    fen_update(a, c, (-a + 1) * c)
    fen_update(b + 1, -c, b * c)

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    fen = [0] * (n + 1)
    fen_cache = [0] * (n + 1)
    
    for _ in range(1, n + 1):
        num = int(input())
        range_update(_, _, num)
        
    for _ in range(m + k):
        com, *pack = map(int, input().split())
        if com == 1:
            range_update(pack[0], pack[1], pack[2])
        else: # com == 2
            print(fen_sum(pack[1]) - fen_sum(pack[0] - 1))

''' 팬위트리 하나로 풀기 -> 시간초과
if __name__ == '__main__':
    n, m, k = map(int, input().split())
    nums = [0]
    cache = [0] * (n + 1)
    fen = [0] * (n + 1)
    for _ in range(n):
        nums.append(int(input()))
    
    cache[1] = nums[1]
    for _ in range(2, n + 1):
        cache[_] = nums[_] - nums[_ - 1]
    
    for _ in range(1, n + 1):
        fen_update(_, cache[_])
    
    for _ in range(m + k):
        com, *pack = map(int, input().split())
        if com == 1:
            fen_update(pack[0], pack[2])
            if pack[1] != n:
                fen_update(pack[1] + 1, pack[2])
        else: # com == 2
            print(fen_sum(pack[0]) - fen_sum(pack[1]))
'''
    
