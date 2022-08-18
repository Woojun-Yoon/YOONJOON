from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 9)
input = stdin.readline

def dfs(n):
    global count
    vis[n] = count
    g[n].sort()
    for _ in g[n]:
        if vis[_] == 0:
            count += 1
            dfs(_)

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    vis = [0] * (n + 1)
    count = 1

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    dfs(r)

    for _ in range(1, n + 1):
        print(vis[_])
