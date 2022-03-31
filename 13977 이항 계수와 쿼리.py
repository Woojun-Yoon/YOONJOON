from sys import stdin
input = stdin.readline
limit = 1000000007

def power(a, b):
    if b == 0:
        return 1
    if (b % 2) == 1:
        return (power(a, b - 1) * a) % limit
    
    half = power(a, b // 2) % limit
    return half * half % limit

fac = [0] * 4000010
reverse_fac = [0] * 4000010
fac[0] = 1
for i in range(1, 4000010):
    fac[i] = fac[i - 1] * i % limit

reverse_fac[4000010 - 1] = power(fac[4000010 - 1], limit - 2)

for j in range(4000010 - 2, -1, -1):
    reverse_fac[j] = reverse_fac[j + 1] * (j + 1) % limit

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = fac[n]
    B = (reverse_fac[n - k] * reverse_fac[k]) % limit
    print(A * B % limit)















''' 시간초과
for _ in range(int(input())):
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
'''
