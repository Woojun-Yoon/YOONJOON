from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    n_s = [*map(int, input().split())]
    cost = [*map(int, input().split())]

    result = 0
    cache = cost[0]
    for _ in range(n - 1):
        if cost[_] < cache:
            cache = cost[_]
        result += cache * n_s[_]
    
    print(result)
