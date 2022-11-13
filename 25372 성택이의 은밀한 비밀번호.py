from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        l = len(input().rstrip())
        if (6 <= l <= 9):
            print("yes")
        else:
            print("no")