from sys import stdin
input = stdin.readline

def fen_xor(index):
    if index == 0:
        return 0
    result = 0
    while index > 0:
        result ^= fen[index]
        index -= (index & -index)
    return result

def fen_update(index, cache):
    while index < len(fen):
        fen[index] ^= cache
        index += (index & -index)

if __name__ == '__main__':
    n = int(input()) # 수열의 크기
    fen = [0] * (n + 1)
    cache = [0] * (n + 1)
    nums = [0] + list(map(int, input().split()))

    cache[1] = nums[1]
    for _ in range(2, n + 1):
        cache[_] = nums[_] ^ nums[_ - 1]

    for _ in range(1, n + 1):
        fen_update(_, cache[_])
    
    m = int(input()) # 쿼리의 개수
    for _ in range(m):
        command, *query = map(int, input().split())
        if command == 1:
            i, j, k = query
            fen_update(i + 1, k)
            if j != n: 
                fen_update(j + 2, k)
        else: # command == 2
            print(fen_xor(query[0] + 1))