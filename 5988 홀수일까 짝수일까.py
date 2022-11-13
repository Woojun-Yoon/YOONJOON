from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        num = int(input())
        if (num % 2 == 0):
            print("even")
        else:
            print("odd")