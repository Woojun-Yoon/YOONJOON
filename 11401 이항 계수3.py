from sys import stdin
input = stdin.readline
limit = 1000000007

n, k = map(int, input().split())
if n - k < k:
    k = n - k

if k == 0:
    print(1)
    quit()

top = n
bottom = 1
for i in range(1, k):
    top = top * (n - i) % limit
    bottom = bottom * (i + 1) % limit

print(top * pow(bottom, -1, limit) % limit)