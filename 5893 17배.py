from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input().rstrip(), 2)
    print(format(n * 17, 'b'))