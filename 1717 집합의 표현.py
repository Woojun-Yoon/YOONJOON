from sys import stdin
input = stdin.readline

def find(n):
    if nums[n] < 0:
        return n
    x = find(nums[n])
    nums[n] = x
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    
    if nums[x] < nums[y]:
        nums[x] += nums[y]
        nums[y] = x
    else:
        nums[y] += nums[x]
        nums[x] = y

if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = [-1 for _ in range(n + 1)]

    for _ in range(m):
        c, a, b = map(int, input().split())
        if c: # c == 1
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
        else: # c == 0
            union(a, b)
