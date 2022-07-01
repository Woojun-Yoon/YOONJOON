from sys import stdin
input = stdin.readline

def diffusion():
    dust_set = []
    # find dust
    for r in range(R):
        for c in range(C):
            if room[r][c] < 5:
                continue
            else:
                move_dust = room[r][c] // 5
                dust_set.append([r, c, move_dust])

    for dust in dust_set:
        r, c, move_dust = dust[0], dust[1], dust[2]
        
        if move_dust == 0:
            continue
        
        move_count = 0
        if c > 0: # diffusion left
            if room[r][c - 1] != -1:
                room[r][c - 1] += move_dust
                move_count += 1
        if r > 0: # diffusion up
            if room[r - 1][c] != -1:
                room[r - 1][c] += move_dust
                move_count += 1
        if c < C - 1: # diffusion right
            room[r][c + 1] += move_dust
            move_count += 1
        if r < R - 1: # diffusion down
            if room[r + 1][c] != -1:
                room[r + 1][c] += move_dust
                move_count += 1
        
        room[r][c] -= move_dust * move_count


def cleaning():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    cache = 0
    x, y = air_cleaner, 1

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]

        if x == air_cleaner and y == 0:
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
            
        room[x][y], cache = cache, room[x][y]
        x = nx
        y = ny
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    cache = 0
    x, y = air_cleaner + 1, 1

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_cleaner + 1 and y == 0:
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue

        room[x][y], cache = cache, room[x][y]
        x = nx
        y = ny

if __name__ == '__main__':
    R, C, T = map(int, input().split()) # (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000)
    room = [[*map(int, input().split())] for _ in range(R)]
    air_cleaner = 0
    for _ in range(R): # search air cleaning
        if room[_][0] == -1:
            air_cleaner = _
            break

    for _ in range(T): # T's running
        diffusion()
        cleaning()
    
    result = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                result += room[i][j]

    print(result)

