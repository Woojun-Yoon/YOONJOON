from sys import stdin
input = stdin.readline

def check(r, c, d, count):
    for _ in range(4):    
        if d == 0:
            if not room[r][c - 1]: # north
                d = 3
                return r, c - 1, d, count
            else:
                d = 3
                count += 1
        elif d == 1:
            if not room[r - 1][c]: # east
                d = 0
                return r - 1, c, d, count
            else:
                d = 0
                count += 1
        elif d == 2:
            if not room[r][c + 1]: # south
                d = 1
                return r, c + 1, d, count
            else:
                d = 1
                count += 1
        elif d == 3:
            if not room[r + 1][c] : # west
                d = 2
                return r + 1, c, d, count
            else:
                d = 2
                count += 1
    
    return r, c, d, count

if __name__ == '__main__':
    n, m = map(int, input().split()) # n = col, m = row
    r, c, d = map(int, input().split()) # current robot's position
    room = [[*map(int, input().split())] for _ in range(n)]
    result = 0

    while True:
        if room[r][c] == 0:
            result += 1
            room[r][c] = 2
        
        count = 0
        r, c, d, count = check(r, c, d, count)
        
        if count == 4:
            if d == 0:
                if room[r + 1][c] != 1:
                    r = r + 1
                else:
                    break
            elif d == 1:
                if room[r][c - 1] != 1:
                    c = c - 1
                else:
                    break
            elif d == 2:
                if room[r - 1][c] != 1:
                    r = r - 1
                else:
                    break
            else:
                if room[r][c + 1] != 1:
                    c = c + 1
                else:
                    break
        
    print(result)

