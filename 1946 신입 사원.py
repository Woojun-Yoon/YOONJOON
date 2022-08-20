from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        n_s = [[*map(int, input().split())] for _ in range(n)]
        n_s.sort(key = lambda x : x[0])
        count = 1
        cache = n_s[0][1]
        for _ in range(1, n):
            if n_s[_][1] < cache:
                cache = n_s[_][1]
                count += 1
        print(count)