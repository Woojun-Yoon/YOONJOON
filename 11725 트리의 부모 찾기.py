from sys import stdin
from sys import setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 9)

def dfs(start, tree, parents):
    for _ in tree[start]:
        if parents[_] == 0:
            parents[_] = start
            dfs(_, tree, parents)


if __name__ == '__main__':
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    parents = [0 for _ in range(n + 1)]

    for _ in range(n - 1):
        num1, num2 = map(int, input().split())
        tree[num1].append(num2)
        tree[num2].append(num1)
    
    dfs(1, tree, parents)

    for _ in range(2, n + 1):
        print(parents[_])
