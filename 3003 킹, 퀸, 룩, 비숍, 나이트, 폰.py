from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    chess = [*map(int, input().split())]
    check = [1, 1, 2, 2, 2, 8]
    for _ in range(6):
        chess[_] = check[_] - chess[_]

    print(*chess)