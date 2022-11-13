from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    cache = 0
    while (True):
        n = int(input())
        if (n == -1):
            break
        else:
            cache += n
    print(cache)