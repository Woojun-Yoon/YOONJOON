from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())

    l = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if r1 + r2 > l:
        print("YES")
    else:
        print("NO")