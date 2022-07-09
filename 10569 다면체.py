from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    for _ in range(int(input())):
        v, e = map(int, input().split())
        print(2 - v + e)