from sys import stdin
input = stdin.readline
L = 1000000000

def seg_min(start, end, index):
    if start == end:
        tree[index] = nums[start - 1]
        return tree[index]
    else:
        mid = (start + end) // 2
        tree[index] = min(seg_min(start, mid, index * 2), seg_min(mid + 1, end, index * 2 + 1))
        return tree[index]

def min_find(start, end, left, right, index):
    if start > right or end < left:
        return L
    
    if start >= left and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return min(min_find(start, mid, left, right, index * 2), min_find(mid + 1, end, left, right, index * 2 + 1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = []
    tree = [0] * (n * 4)
    for _ in range(n):
        nums.append(int(input()))
    
    seg_min(1, n, 1)

    for _ in range(m):
        a, b = map(int, input().split())
        print(min_find(1, n, a, b, 1))
    

    
