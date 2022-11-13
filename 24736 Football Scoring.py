from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(a[0] * 6 + a[1] * 3 + a[2] * 2 + a[3] * 1 + a[4] * 2, b[0] * 6 + b[1] * 3 + b[2] * 2 + b[3] * 1 + b[4] * 2)