from sys import stdin
input = stdin.readline

n = int(input())
a = sorted([item for item in map(int, input().split())])
b = sorted([item for item in map(int, input().split())])
result = 0
for i in range(n):
    result += a[i] * b[n - 1 - i]
print(result)