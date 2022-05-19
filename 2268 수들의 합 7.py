from sys import stdin
from math import ceil, log2
input = stdin.readline

# use python3
# use Fenwick Tree -> disadvantage = min,max searching, advantage -> special sum, update
# 
n, m = map(int, input().split())
tree = [0] * (n + 1)
nums = [0] * (n + 1)

def tree_sum(index):
    result = 0
    while index > 0:
        result += tree[index]
        index -= (index & -index)
    return result

def tree_update(index, cache):
    while index < len(tree):
        tree[index] += cache
        index += (index & -index)

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        tree_update(b, c - nums[b])
        nums[b] = c
        print(tree)
        print(nums)
    else: # a == 2
        if c < b:
            print(tree_sum(b) - tree_sum(c - 1))
        else:
            print(tree_sum(c) - tree_sum(b - 1))

# use pypy3
'''
def seg_sum(start, end, left, right, index):
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    all_sum = seg_sum(start, mid, left, right, index * 2) + seg_sum(mid + 1, end, left, right, index * 2 + 1)
    return all_sum

def seg_update(start, end, index, cache_index, cache_data):
    if start > cache_index or end < cache_index:
        return
    
    tree[index] += cache_data

    if start == end:
        return
    
    mid = (start + end) // 2
    seg_update(start, mid, index * 2, cache_index, cache_data)
    seg_update(mid + 1, end, index * 2 + 1, cache_index, cache_data)

if __name__ == "__main__":
    n, m = map(int, input().split()) # n : 개수, m : 명령어의 개수
    tree_size = int(ceil(log2(n)))
    tree = [0] * 2 ** (tree_size + 1)
    nums = [0] * n

    for _ in range(m): # 명령어 실행
        a, b ,c = map(int, input().split())
        if a == 0: # seg_sum
            if c < b:
                print(seg_sum(1, n, c, b, 1))
            else:
                print(seg_sum(1, n, b, c, 1))
        else: # a == 1 , seg_update
            cache = c - nums[b - 1]
            nums[b - 1] = c
            seg_update(1, n, 1, b, cache)
'''