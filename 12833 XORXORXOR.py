from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())
if c % 2 == 1:
    print(a ^ b)
else:
    print(a)