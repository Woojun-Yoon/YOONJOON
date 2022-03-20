from sys import stdin
from itertools import product
input = stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
num_list = map(str, num_list)
for result in product(num_list, repeat = m):
    print(*result)

# map과 join으로 더 빨리풀기

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
num_list = map(str, num_list)
result = map(' '.join, product(num_list, repeat = m))
print('\n'.join(result))