from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
board = []
dis = [[0 for x in range(m)] for y in range(n)]
dis[0][0] = 1
for _ in range(n):
    board.append(list(input()))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Q = deque([])
Q.append((0,0))
while(Q):
    cur = Q.popleft()
    for k in range(4):
        nx = cur[0] + dx[k]
        ny = cur[1] + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dis[nx][ny] == 0 and board[nx][ny] == '1':
                dis[nx][ny] = dis[cur[0]][cur[1]] + 1
                Q.append((nx, ny))
print(dis[n - 1][m - 1])






