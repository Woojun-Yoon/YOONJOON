from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    a = sum(list(map(int, input().split())))
    b = sum(list(map(int, input().split())))
    if (a > b):
        print(a)
    else:
        print(b)