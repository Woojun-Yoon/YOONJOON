from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    print((n // 100) * 78, n - (((n // 100) * 20) // 100) * 22)