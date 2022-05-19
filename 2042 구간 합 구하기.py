from sys import stdin
from math import ceil, log2
input = stdin.readline

def seg(node, start, end):
    if start == end:
        tree[node] = nums[start - 1]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = seg(node * 2, start, mid) + seg(node * 2 + 1, mid + 1, end)
        return tree[node]

def find(start, end, index, left, right): # 구간합 구하기
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    tree_sum = find(start, mid, index * 2, left, right) + find(mid + 1, end, index * 2 + 1, left, right)
    return tree_sum

def update(start, end, index, cache_index, cache_data): # 해당 index에 해당하는 tree 모두 update
    if start > cache_index or end < cache_index:
        return
    
    tree[index] += cache_data
    
    if start == end:
        return
    
    mid = (start + end) // 2
    update(start, mid, index*2, cache_index, cache_data)
    update(mid+1, end, index*2+1, cache_index, cache_data)

n, m, k = map(int, input().split())
nums = []
# tree 크키 정확하게 구하기(매우 정확하지는 않음)
tree_size = int(ceil(log2(n)))
tree = [0] * 2 ** (tree_size + 1)

''' tree 크기 편하게 구하기 속도 우선시
tree = [0] * (n * 4)
'''
for _ in range(n):
    nums.append(int(input()))

seg(1, 1, n)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        cache = c - nums[b - 1]
        nums[b - 1] = c
        update(1, n, 1, b, cache)
    else: # a == 2
        print(find(1, n, 1, b, c))