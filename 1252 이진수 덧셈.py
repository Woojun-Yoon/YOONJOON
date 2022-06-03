from sys import stdin
input = stdin.readline

a, b = input().split()
result = int(a, 2) + int(b, 2)
print(format(result, 'b'))