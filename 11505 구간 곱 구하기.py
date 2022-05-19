from sys import stdin
input = stdin.readline

L = 1000000007

def seg(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = seg(start, mid, node * 2) * seg(mid + 1, end, node * 2 + 1) % L
        return tree[node]

def seg_mul(start, end, left, right, index):
    if start > right or end < left:
        return 1
    
    if start >= left and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    tree_mul = seg_mul(start, mid, left, right, index * 2) * seg_mul(mid + 1, end, left, right, index * 2 + 1) % L
    return tree_mul

def seg_update(start, end, index, cache_index, cache_data):
    if start > cache_index or end < cache_index:
        return
 
    if start == end:
        tree[index] = cache_data
        return 
    
    mid = (start + end) // 2
    seg_update(start, mid, index * 2, cache_index, cache_data)
    seg_update(mid + 1, end, index * 2 + 1, cache_index, cache_data)

    tree[index] = tree[index * 2] * tree[index * 2 + 1] % L
    return 

if __name__ == '__main__':
      
    n, m, k = map(int, input().split())
    nums = [0] + list(int(input()) for _ in range(n))
    tree = [0] * (n * 4)

    seg(1, n, 1) # 세그먼트 트리 생성

    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            # update
            seg_update(1, n, 1, b, c)
            nums[b] = c
        else: # a == 2
            # print mul
            print(seg_mul(1, n, b, c, 1))