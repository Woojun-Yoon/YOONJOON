from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    while (True):
        a, b = map(int, input().split())
        if (a == 0 and b == 0):
            break
        else:
            print(a + b)