from sys import stdin
input = stdin.readline
# use fenwick

def fen_sum(index):
    result = 0
    while index > 0:
        result += tree[index]
        index -= (index & -index)
    return result

def fen_update(index, cache):
    while index < n + 1:
        tree[index] += cache
        index += (index & -index)


if __name__ == '__main__':
    n, q = map(int, input().split())
    nums = [0] + list(map(int, input().split()))
    tree = [0] * (n + 1)

    for _ in range(1, n + 1):
        fen_update(_, nums[_])
    
    for _ in range(q):
        x, y, a, b = map(int, input().split())
        # print
        if x > y:
            print(fen_sum(x) - fen_sum(y - 1))
        else:
            print(fen_sum(y) - fen_sum(x - 1))
        # update
        fen_update(a, b - nums[a])
        nums[a] = b