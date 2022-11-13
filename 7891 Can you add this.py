from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(a + b)