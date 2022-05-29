from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    D, H, W = map(int, input().split())
    D = D ** 2
    cache1 = H ** 2 + W ** 2
    cache2 = D / cache1
    cache2 = cache2 ** 0.5

    print(int(H * cache2), int(W * cache2))
