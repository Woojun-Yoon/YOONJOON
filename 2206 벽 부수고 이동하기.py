from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    q = deque()
    q.append([0, 0, 1])
    vis = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    vis[0][0][1] = 1

    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return vis[a][b][w]
        
        for _ in range(4):
            x = a + dx[_]
            y = b + dy[_]
            if 0 <= x < n and 0 <= y < m:
                if board[x][y] == 1 and w == 1:
                    vis[x][y][0] = vis[a][b][1] + 1
                    q.append([x, y, 0])
                elif board[x][y] == 0 and vis[x][y][w] == 0:
                    vis[x][y][w] = vis[a][b][w] + 1
                    q.append([x, y, w])
    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append([*map(int, input().rstrip())])
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    print(bfs())