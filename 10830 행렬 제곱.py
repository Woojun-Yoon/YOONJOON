from sys import stdin
input = stdin.readline
L = 1000

def multi(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            element = 0
            for _ in range(n):
                element += a[row][_] * b[_][col]
            result[row][col] = element % L
    return result

def power(a, b): # b = power
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= L
        return a
    
    cache = power(a, b // 2)

    if b % 2: # b = odd
        return multi(multi(cache, cache), a)
    else: # b = even
        return multi(cache, cache)

if __name__ == '__main__':
    n, b = map(int, input().split())
    a = [[*map(int, input().split())] for _ in range(n)]

    result = power(a, b)

    for _ in result:
        print(*_)