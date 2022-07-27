from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    k = int(input())
    d1, d2 = map(int, input().split())
    h = k ** 2 - ((abs(d1 - d2)) / 2) ** 2
    print(h)