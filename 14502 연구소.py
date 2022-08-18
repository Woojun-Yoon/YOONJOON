from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
area = []
cache = [[0] * m for _ in range(n)]

for _ in range(n):
    area.append([*map(int, input().split())])
# W, N, E, S
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def spread(x, y):
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]

        if 0 <= nx < n and 0 <= ny < m:
            if cache[nx][ny] == 0:
                cache[nx][ny] = 2
                spread(nx, ny)
    return

def score():
    res = 0
    for i in range(n):
        for j in range(m):
            if cache[i][j] == 0:
                res += 1
    return res

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                cache[i][j] = area[i][j]
        
        for i in range(n):
            for j in range(m):
                if cache[i][j] == 2:
                    spread(i, j)
        
        result = max(result, score())
        return
    
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                area[i][j] = 1
                count += 1
                dfs(count)
                area[i][j] = 0
                count -= 1

dfs(0)
print(result)


