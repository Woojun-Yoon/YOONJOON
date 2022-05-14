from sys import stdin
input = stdin.readline
limit = 10007

n, r = map(int, input().split())
if n - r < r:
    r = n - r

if r == 0:
    print(1); quit()

top = n
bottom = 1

for i in range(1, r):
    top = top * (n - i) % limit
    bottom = bottom * (i + 1) % limit

print(top * pow(bottom, -1, limit) % limit)