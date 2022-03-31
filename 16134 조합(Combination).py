from sys import stdin
input = stdin.readline
limit = 1000000007
''' n의 최대값 만큼 배열을 만든 후 분할 정복 거듭제곱으로 풀이 770ms
def power(a, b):
    if b == 0:
        return 1
    if (b % 2) == 1:
        return (power(a, b - 1) * a) % limit
    
    half = power(a, b // 2) % limit
    return half * half % limit

n, r = map(int, input().split())

fac = [0] * 1000010
reverse_fac = [0] * 1000010
fac[0] = 1
for i in range(1, 1000010):
    fac[i] = fac[i - 1] * i % limit

reverse_fac[1000010 - 1] = power(fac[1000010 - 1], limit - 2)

for j in range(1000010 - 2, -1, -1):
    reverse_fac[j] = reverse_fac[j + 1] * (j + 1) % limit

A = fac[n]
B = (reverse_fac[n - r] * reverse_fac[r]) % limit
print(A * B % limit)
'''
# 220ms
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

print(top * pow(bottom, -1, limit) % limit) # pow 3번째 인자 = mod