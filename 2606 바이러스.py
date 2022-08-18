from sys import stdin
input = stdin.readline

def dfs(start, g):
    for _ in g[start]:
        if _ not in vis:
            vis.append(_)
            dfs(_, g)

if __name__ == '__main__':
    graph = {}
    vis = []

    for _ in range(int(input())):
        graph[_ + 1] = set()
    for _ in range(int(input())):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    
    dfs(1, graph)
    print(len(vis) - 1)