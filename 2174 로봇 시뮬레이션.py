from sys import stdin
input = stdin.readline
"""
def L(way, repeat):
    for _ in range(repeat):
        if way == 'N':
            way = 'W'
        elif way == 'E':
            way = 'N'
        elif way == 'S':
            way = 'E'
        else: # way == 'W'
            way = 'S'
    return way

def R(way, repeat):
    for _ in range(repeat):
        if way == 'N':
            way = 'E'
        elif way == 'E':
            way = 'S'
        elif way == 'S':
            way = 'W'
        else: # way == 'W'
            way = 'N'
    return way

def F(x, y, way):
    if way == 'N':
        return x, y + 1
    elif way == 'E':
        return x + 1, y
    elif way == 'S':
        return x, y - 1
    else: # way == 'W'
        return x - 1, y

if __name__ == '__main__':
    a, b = map(int, input().split()) # a = width, b = length
    n, m = map(int, input().split())
    check = 0
    board = [[0 for _ in range(a)] for _ in range(b)]
    robot = []

    for _ in range(n):
        robot.append(input().split())
        board[int(robot[_][1]) - 1][int(robot[_][0]) - 1] = _ + 1
    for _ in range(m):
        select, command, repeat = input().split()

        if command == 'L':
            robot[int(select) - 1][2] = L(robot[int(select) - 1][2], int(repeat))
        elif command == 'R':
            robot[int(select) - 1][2] = R(robot[int(select) - 1][2], int(repeat))
        else: # command == 'F'
            x, y, way = robot[int(select) - 1]
            cache = board[int(y) - 1][int(x) - 1]
            board[int(y) - 1][int(x) - 1] = 0
            for _ in range(int(repeat)):
                x, y = F(int(x), int(y), way)
                if x > a or y > b or x < 0 or y < 0:
                    check = 1
                    print("Robot", select, "crashes into the wall")
                    break

                if board[y - 1][x - 1] > 0:
                    check = 1
                    print("Robot", select, "crashes into robot", board[y - 1][x - 1])
                    break
                
            if check == 0:
                board[y - 1][x - 1] = cache
                robot[int(select) - 1][0] = x
                robot[int(select) - 1][1] = y
        if check == 1:
            break

    if check == 0:
        print("OK")
"""
def rotation_left(d):  # 왼쪽으로 90도 회전
    if d == "N":
        return "W"
    elif d == "W":
        return "S"
    elif d == "S":
        return "E"
    elif d == "E":
        return "N"


def rotation_right(d):  # 오른쪽으로 90도 회전
    if d == "N":
        return "E"
    elif d == "E":
        return "S"
    elif d == "S":
        return "W"
    elif d == "W":
        return "N"


def check(x, y):
    if d == "N":
        if x - 1 < 0:
            return 'wall'
        elif maps[x - 1][y]:
            return 'robot'
        else:
            return True
    elif d == "W":
        if y - 1 < 0:
            return 'wall'
        elif maps[x][y - 1]:
            return 'robot'
        else:
            return True
    elif d == "S":
        if x + 1 >= B:
            return 'wall'
        elif maps[x + 1][y]:
            return 'robot'
        else:
            return True
    elif d == "E":
        if y + 1 >= A:
            return 'wall'
        elif maps[x][y + 1]:
            return 'robot'
        else:
            return True


def move(x, y, d):
    if d == "N":
        return x - 1, y, d
    elif d == "W":
        return x, y - 1, d
    elif d == "S":
        return x + 1, y, d
    elif d == "E":
        return x, y + 1, d


if __name__ == "__main__":
    A, B = map(int, input().split())
    N, M = map(int, input().split())
    maps = [[None] * A for _ in range(B)]
    robot = dict()
    for i in range(N):  # 로봇의 초기 위치 및 방향 입력
        x, y, d = input().split()
        x, y = int(x), int(y)
        maps[B - y][x - 1] = [d, i + 1]
        robot[i + 1] = [B - y, x - 1, d]

    flag = True
    for i in range(M):  # 명령 수행
        if flag:
            number, order, cnt = input().split()
            number, cnt = int(number), int(cnt)
            for _ in range(cnt):
                if flag:
                    x, y, d = robot[number]
                    if order == "L":
                        d = rotation_left(d)
                        robot[number] = [x, y, d]
                    elif order == "R":
                        d = rotation_right(d)
                        robot[number] = [x, y, d]
                    elif order == "F":
                        temp = check(x, y)
                        if temp == 'wall':
                            print("Robot {} crashes into the wall".format(number))
                            flag = False
                            break
                        elif temp == 'robot':
                            x, y, d = move(x, y, d)
                            print("Robot {} crashes into robot {}".format(number, maps[x][y][1]))
                            flag = False
                            break
                        else:
                            maps[x][y] = None
                            x, y, d = move(x, y, d)
                            robot[number] = x, y, d
                            maps[x][y] = [d, number]

    # 출력
    if flag:
        print("OK")