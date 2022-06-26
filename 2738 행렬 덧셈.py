from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    col, low = map(int, input().split())

    cache1 = []
    for _ in range(col):
        cache1.append(list(map(int, input().split())))
    
    cache2 = []
    for _ in range(col):
        cache2.append(list(map(int, input().split())))

    for i in range(col):
        for j in range(low):
            cache1[i][j] = cache1[i][j] + cache2[i][j]
    
    for _ in range(col):
        print(*cache1[_])