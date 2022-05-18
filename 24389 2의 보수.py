from sys import stdin
input = stdin.readline

n = int(input())
cache = int('1' * 32, 2)
cache1 = format(n, 'b').zfill(32)
cache2 = format((n ^ cache) + 1, 'b').zfill(32)

cache3 = n ^ int(cache2, 2)
cache3 = format(cache3, 'b').zfill(32)

count = 0

for _ in range(32):
    if cache3[_] == '1':
        count += 1
    
print(count)