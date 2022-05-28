from sys import stdin
input = stdin.readline

def seg(start, end, index):
    if start == end:
        tree[index] = [nums[start], start]
    else:
        mid = (start + end) // 2
        seg(start, mid, index * 2)
        seg(mid + 1, end, index * 2 + 1)

        if tree[index * 2][0] > tree[index * 2 + 1][0]:
            small = index * 2 + 1
        else:
            small = index * 2

        tree[index] = [tree[small][0], tree[small][1]]

def seg_update(start, end, left, right, index, cache):
    if start > right or end < left:
        return
    
    if start >= left and end <= right:
        tree[index] = [cache, start]
        return
    
    mid = (start + end) // 2
    seg_update(start, mid, left, right, index * 2, cache)
    seg_update(mid + 1, end, left, right, index * 2 + 1, cache)

    if tree[index * 2][0] > tree[index * 2 + 1][0]:
        small = index * 2 + 1
    else:
        small = index * 2
    
    tree[index] = [tree[small][0], tree[small][1]]


if __name__ == '__main__':
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    tree = [[0, 0]] * (4 * n)
    seg(1, n, 1)

    for _ in range(int(input())):
        command, *update = map(int, input().split())
        if command == 1:
            seg_update(1, n, update[0], update[0], 1, update[1])
        else:
            print(tree[1][1])