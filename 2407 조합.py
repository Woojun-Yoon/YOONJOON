from sys import stdin
input = stdin.readline
fac = [0] * 101
fac[0] = 1
fac[1] = 1
n, m = map(int, input().split())
for _ in range(2, 101):
    fac[_] = _ * fac[_ - 1]

print((fac[n] // fac[m]) // fac[n - m])