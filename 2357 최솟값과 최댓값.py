from sys import stdin
input = stdin.readline

def seg_max(start, end, index):
    if start == end:
        tree_max[index] = nums[start - 1]
        return tree_max[index]
    else:
        mid = (start + end) // 2
        tree_max[index] = max(seg_max(start, mid, index * 2), seg_max(mid + 1, end, index * 2 + 1))
        return tree_max[index]

def seg_min(start, end, index):
    if start == end:
        tree_min[index] = nums[start - 1]
        return tree_min[index]
    else:
        mid = (start + end) // 2
        tree_min[index] = min(seg_min(start, mid, index * 2), seg_min(mid + 1, end, index * 2 + 1))
        return tree_min[index]

def max_find(start, end, left, right, index):
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return tree_max[index]
    
    mid = (start + end) // 2
    return max(max_find(start, mid, left, right, index * 2), max_find(mid + 1, end, left, right, index * 2 + 1))

def min_find(start, end, left, right, index):
    if start > right or end < left:
        return 1000000001
    
    if start >= left and end <= right:
        return tree_min[index]
    
    mid = (start + end) // 2
    return min(min_find(start, mid, left, right, index * 2), min_find(mid + 1, end, left, right, index * 2 + 1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = []
    tree_max = [0] * (n * 4)
    tree_min = [0] * (n * 4)
    for _ in range(n):
        nums.append(int(input()))
    
    seg_max(1, n, 1)
    seg_min(1, n, 1)

    for _ in range(m):
        left, right = map(int, input().split())
        print(min_find(1, n, left, right, 1), max_find(1, n, left, right, 1))
