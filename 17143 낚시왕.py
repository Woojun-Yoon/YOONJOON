from sys import stdin
input = stdin.readline

def move():
    cache = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if sea[x][y] != 0:
                i, j, s, d, z = x, y, sea[x][y][0], sea[x][y][1], sea[x][y][2]
                while s > 0:
                    j += dy[d]
                    i += dx[d]
                    if 0 <= i < r and 0 <= j < c:
                        s -= 1
                    else:
                        j -= dy[d]
                        i -= dx[d]
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        else:
                            d = 2
                if cache[i][j] == 0:
                    cache[i][j] = [sea[x][y][0], d, z]
                else:
                    if cache[i][j][2] < z:
                        cache[i][j] = [sea[x][y][0], d, z]
    return cache



if __name__ == '__main__':
    r, c, m = map(int, input().split())
    sea = [[0] * c for _ in range(r)]
    result = 0

    for _ in range(m):
        i, j, s, d, z = map(int, input().split())
        sea[i - 1][j - 1] = [s, d - 1, z]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for x in range(c):
        for y in range(r):
            if sea[y][x] != 0:
                result += sea[y][x][2]
                sea[y][x] = 0
                break
        sea = move()

    print(result)