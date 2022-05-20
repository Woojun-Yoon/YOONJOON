from sys import stdin
input = stdin.readline

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

n = int(input())
nums = [0] + list(map(int, input().split()))
tree = [0] * (n + 1)
penwick = [0] * (n + 1)
penwick[1] = nums[1]
for num in range(2, len(nums)):
    penwick[num] = nums[num] - nums[num - 1]

for i in range(1, n + 1):
    tree_update(i, penwick[i])

m = int(input()) # 쿼리의 수
for _ in range(m):
    a, *command = map(int, input().split())
    if a == 1:
        # sum
        i, j, k = command
        tree_update(i, k)
        penwick[i] = k
        if (j != len(penwick) - 1):
            tree_update(j + 1, - k)
            penwick[j + 1] = -k
    else: # a == 2
        # print
        print(tree_sum(command[0]))