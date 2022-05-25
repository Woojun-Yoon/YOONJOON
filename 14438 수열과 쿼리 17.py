from sys import stdin
input = stdin.readline

def seg_min(start, end ,index):
    if start == end:
        tree[index] = nums[start - 1]
        return tree[index]
    else:
        mid = (start + end) // 2
        tree[index] = min(seg_min(start, mid, index * 2), seg_min(mid + 1, end, index * 2 + 1))
        return tree[index]

def find_min(start, end, left, right, index):
    if start > right or end < left:
        return 1000000001
    
    if start >= left and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return min(find_min(start, mid, left, right, index * 2), find_min(mid + 1, end, left, right, index * 2 + 1))

def min_update(start, end, index, cache_index, cache_data):
    if start > cache_index or end < cache_index:
        return
    
    if start == end:
        tree[index] = cache_data
        return
    mid = (start + end) // 2
    min_update(start, mid, index * 2, cache_index, cache_data)
    min_update(mid + 1, end, index * 2 + 1, cache_index, cache_data)

    tree[index] = min(tree[index * 2], tree[index * 2 + 1])
    return



if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    tree = [0] * (n * 4)
    m = int(input())
    seg_min(1, n, 1)
    for _ in range(m):
        query, i, j = map(int, input().split())
        if query == 1: # update
            min_update(1, n, 1, i, j)
        else: # query == 2 # find_ min
            print(find_min(1, n, i, j, 1))