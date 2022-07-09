from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n, w, h = map(int, input().split())
    max_len = (w ** 2 + h ** 2) ** 0.5
    for _ in range(n):
        if int(input()) <= max_len:
            print("DA")
        else:
            print("NE")