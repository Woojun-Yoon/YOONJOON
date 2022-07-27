from sys import stdin
input = stdin.readline

def dfs(n):
    if n == 81:
        for _ in board:
            print(''.join(map(str, _)))
        return 1
    
    x = n // 9
    y = n % 9
    if board[x][y]:
        return dfs(n + 1)
    else:
        for _ in range(1, 10):
            if not c1[x][_] and not c2[y][_] and not c3[(x // 3) * 3 + (y // 3)][_]:
                c1[x][_] = c2[y][_] = c3[(x // 3) * 3 + (y // 3)][_] = 1
                board[x][y] = _

                if dfs(n + 1):
                    return 1
                else:
                    c1[x][_] = c2[y][_] = c3[(x // 3) * 3 + (y // 3)][_] = 0
                    board[x][y] = 0
    return 0

if __name__ == '__main__':
    N = 9
    board = [[*map(int, input().rstrip())] for _ in range(N)]
    
    c1 = [[0] * 10 for _ in range(N)] # low
    c2 = [[0] * 10 for _ in range(N)] # col
    c3 = [[0] * 10 for _ in range(N)] # box

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                c1[i][board[i][j]] = 1
                c2[j][board[i][j]] = 1
                c3[(i // 3) * 3 + (j // 3)][board[i][j]] = 1
    
    dfs(0)