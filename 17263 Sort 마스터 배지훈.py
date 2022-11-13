from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    print(max([*map(int, input().split())]))