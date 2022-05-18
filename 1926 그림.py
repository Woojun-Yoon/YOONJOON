from sys import stdin
from collections import deque
input = stdin.readline

photo_count = 0
photo_max = 0

n, m = map(int, input().split()) # n = 세로, m = 가로
vis = [[0 for col in range(m)] for row in range(n)]
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1] 

for i in range(n):
    for j in range(m):
        if ((board[i][j] == 0) or (vis[i][j])):
            continue
        
        photo_count += 1
        vis[i][j] = 1
        photo_Q = deque([])
        photo_Q.append((i,j))
        photo_area = 0

        while(photo_Q):
            photo_area += 1
            cache = photo_Q.popleft()
            x = cache[0]
            y = cache[1]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 1 and not vis[nx][ny]:
                        vis[nx][ny] = 1
                        photo_Q.append((nx, ny))
                        
        
        photo_max = max(photo_max, photo_area)

print(photo_count)
print(photo_max)