from sys import stdin
input = stdin.readline

coin = []
result = 0
n, k = map(int, input().split())
for _ in range(n):
    coin.append(int(input()))

n = n - 1

while True:
    if k == 0:
        break
    
    if coin[n] > k:
        n = n - 1
        continue
    else:
        count = k // coin[n]
        result += count
        k -= count * coin[n]
        n = n - 1
print(result)